from flask import Flask, render_template, request, jsonify
from carbon_footprint_model import CarbonFootprintCalculator

app = Flask(__name__)
calculator = CarbonFootprintCalculator()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate carbon footprint based on form data."""
    try:
        # Get form data
        electricity = float(request.form.get('electricity', 300))
        transport = float(request.form.get('transport', 200))
        meat = float(request.form.get('meat', 1.5))
        waste = float(request.form.get('waste', 5))
        water = float(request.form.get('water', 150))
        region = request.form.get('region', '')
        
        # Calculate footprint
        result = calculator.calculate_footprint(electricity, transport, meat, waste, water)
        
        # Get total footprint and level
        total = result['footprints']['total']
        level = calculator.get_footprint_level(total)
        
        # Get regional comparison if provided
        regional_comparison = ""
        if region:
            regional_comparison = calculator.compare_with_region(total, region)
        
        # Format recommendations
        recommendations = {}
        if result['detailed_recommendations']:
            for category, suggestions in result['detailed_recommendations'].items():
                recommendations[category] = suggestions[:3]  # Limit to top 3 recommendations
        
        # Prepare response data
        response_data = {
            'success': True,
            'footprints': result['footprints'],
            'comparisons': result['comparisons'],
            'level': level,
            'recommendations': recommendations,
            'regional_comparison': regional_comparison,
            'global_averages': result['global_averages']
        }
        
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/regions', methods=['GET'])
def get_regions():
    """Return a list of valid regions."""
    regions = list(calculator.regional_averages.keys())
    return jsonify(regions)

if __name__ == '__main__':
    app.run(debug=True) 