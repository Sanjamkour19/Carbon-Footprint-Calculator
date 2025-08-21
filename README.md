# Carbon Footprint Calculator

A Python-based tool to calculate your carbon footprint, compare it with global and regional averages, and provide personalized recommendations for reducing your environmental impact.

## Features

- Calculate carbon footprint based on key consumption metrics
- Compare your footprint with global and regional averages
- Receive personalized recommendations based on your results
- Detailed information about the impact and effort required for each recommendation
- Available as both command-line tool and web application
- User-friendly interfaces with input validation

## How It Works

The calculator takes the following inputs:
- Monthly electricity consumption (kWh)
- Weekly distance traveled by car (km)
- Weekly meat consumption (kg)
- Weekly non-recycled waste (kg)
- Daily water consumption (liters)
- Your geographical region (optional)

Based on these inputs, it calculates:
1. Your carbon footprint for each category
2. Your total carbon footprint in metric tons of CO2 per year
3. How your footprint compares to global and regional averages
4. Whether your usage is high, moderate, or low
5. Personalized recommendations to reduce your carbon footprint

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Required packages (install using `pip install -r requirements.txt`):
  - pandas
  - numpy
  - Flask (for web interface)

### Running the Command Line Interface

1. Clone this repository or download the files
2. Open a terminal/command prompt in the project directory
3. Run the application:

```
python carbon_footprint_app.py
```

4. Follow the prompts to enter your consumption data
5. Review your results and recommendations

### Running the Web Interface

1. Clone this repository or download the files
2. Open a terminal/command prompt in the project directory
3. Install requirements:

```
pip install -r requirements.txt
```

4. Start the web server:

```
python app.py
```

5. Open your web browser and navigate to http://localhost:5000
6. Fill out the form and click "Calculate My Footprint"
7. Review your results and recommendations

## Project Structure

- `carbon_footprint_app.py` - The command-line application
- `carbon_footprint_model.py` - The calculation model and logic
- `carbon_footprint_data.py` - Dataset with emission factors, averages, and recommendations
- `app.py` - Flask web application
- `templates/` - HTML templates for the web interface
- `static/` - CSS, JavaScript, and images for the web interface

## Data Sources

The emission factors and global/regional averages are based on various environmental research studies and databases. The values represent typical emissions for different activities and regions but may vary based on specific local conditions.

## Future Improvements

- More detailed inputs for more accurate calculations
- Ability to save and track progress over time
- Visualization of carbon footprint data over time
- User accounts for tracking changes
- Integration with smart home devices for automatic data collection
- Mobile application

## License

This project is open source and available for educational and personal use.

## Author

Created as a demonstration project for carbon footprint calculation and environmental awareness. 