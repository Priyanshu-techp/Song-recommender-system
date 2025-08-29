# Book Recommander System
The objective this project is the recommend the song and play on real time. And data will extract from Spotify on real time.

---
## Project Structure

```
├── Data/                  
├── notebook/        
│    └── Song_recommender.ipynb       
├── Deploying/
│   ├── song_rec.py            
│   ├── tf_vectorizer.pkl             
│   └── vector.pkl           
├── .cache         
├── Data_extract.py         
├── requirements.txt          
├── README.md
└── .gitignore 
```

## Objective

Create a song recommender system and play on the real time
---

## Features Used
- Track Name
- Artist(s) 
- Spotify URL 
- Artist Name
- Genres
- Album Name
- Album Image URL
---

##  Technologies Used

- Python (Pandas, Scikit-learn)
- Streamlit (for deployment)
- Joblib (for model saving/loading)

---

## How to Run the App

1. Clone the repository:
   ```bash
   git remote add origin https://github.com/Priyanshu-techp/Song-recommender-system.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run 'Deploying/song_rec.py'
   ```
---

## Deploy link
[Streamlit app link](https:/song-recommending-system.streamlit.app/)

## Author

**Priyanshu Pandey**  
Diploma in Automation & Robotics  
Aspiring Data Scientist  
[LinkedIn Profile](https://www.linkedin.com/in/priyanshu-pandey67)