# Hungary's Richest People - Earnings Tracker

A real-time web application that displays Hungary's richest people and their earnings per second. The application features a dynamic counter showing how much money these billionaires make every second based on their net worth and assuming a 5% annual return.

## Features

- Real-time earnings counter
- Individual earnings display for each person
- Time elapsed counter
- Beautiful, responsive design
- Profile pictures for each billionaire

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hungary-richest.git
cd hungary-richest
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add profile pictures:
- Place the profile pictures in the `static/images` folder with the following names:
  - `csanyi.jpg.jpg`
  - `meszaros.jpg.webp`
  - `varszegi.jpg.webp`

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to `http://localhost:5000`

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## Data Source

The net worth data is based on recent estimates of Hungary's richest people. The earnings calculation assumes a 5% annual return on their total net worth. 