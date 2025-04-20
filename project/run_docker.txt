# save api key as environmental variable

nano ~/.bashrc
export API_KEY="your_api_key_here"
source ~/.bashrc



# To run the docker container
docker build -t my_streamlit_app .
docker run -p 8501:8501 -e GOOGLE_GENAI_API_KEY=$GOOGLE_GENAI_API_KEY my-streamlit-app
