# SkillSage

## About

SkillSage is a powerful tool that provides comprehensive data on skills, locations, and salary statistics for various job roles across different countries. Leveraging the Adzuna API, this application offers real-time, data-driven insights to job seekers, employers, and market analysts.

## Features

- **Skill Trends**: Visualize the most in-demand skills for specific job roles.
- **Location Analysis**: Explore job concentrations and opportunities in various regions.
- **Salary Statistics**: Get detailed salary information, including averages, ranges, and comparisons.
- **Dynamic Data**: All information is fetched in real-time from the Adzuna API, ensuring up-to-date insights.

## Installation

1. Clone the repository:
   git clone https://github.com/sthiti24/SkillSage.git
2. Navigate to the project directory: cd SkillSage
3. Install required dependencies: pip install -r requirements.txt
4. Set up your Adzuna API credentials:

- Sign up for an API key at [Adzuna API](https://developer.adzuna.com/)
- Create a `.env` file in the root directory and add your credentials:
  ```
  ADZUNA_APP_ID=your_app_id
  ADZUNA_API_KEY=your_api_key
  MAP_BOX_API_KEY=your_map_box_api_key
  ```

## Usage

1. Run the Streamlit app: streamlit run app.py
2. Open your web browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`).

3. Use the interface to select job roles, countries, and view the generated insights.

## Dependencies

- Python 3.7+
- Streamlit
- Pandas
- Plotly
- Requests
- Geopy

## Contributing

Contributions to improve Job Market Insights are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Sthiti Pragyan Panda - [sthitipragyan24@gmail.com](mailto:sthitipragyan24@gmail.com)

Project Link: [sthiti24/SkillSage](https://github.com/sthiti24/SkillSage)

## Acknowledgements

- [Adzuna API](https://developer.adzuna.com/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
