1. Project Architecture:  
    - Collecting data
    - Feature Extraction
        - Extracting MFCCS
        - Using CNNs probablistic output to generate more features:
            -Handeling Data unbalance by using Stratified K-Fold Cross Validation
            -we usually take the max of the softmax of the last dense layer in Classificatin task , how about we don't ? we get probailities of the other genres present in the track -> more features 
        - Using [vocali.se](https://vocali.se/en) to seperate Audio
        - Working on the Acapella Track (vocals)
          - Speech recognition and Transcribing Lyrics
          - Topic Modeling (NMF and idf-tdf vectorizer)
        - Working on the Karaoke Track (instruments only)
          - Amplitude Envolope
          - Spectral Centroid
          - 0 Crossing rate
          - Spectral Flux
    - Create the user class and fill it with synthetic data
    - Creating Recommendations (Content based)
        - Creating Track Clusters using all the features
        - Using Rule-Association to detect patterns from existing watch histories (A priori algorithm)
        - Recommending The next Song using the same cluster and the rules obtained 
2. Project Idea and motivation:
  I enjoy listening to music while gaming or coding but sometimes the song i'm listening to doesn't exactly fit the mode i'm in .
  I usually put the playlist on shuffle and on average things turn out ok but after having come across Valerio Velardo - The sound of AI youtube Channel, I decided I will
  make my own in-house recommendation system (or try to)
3. Project Technologies:
      - draw.io
      - Bigasoft Total Video Converter
      - Internet Download Manager
      - https://vocali.se/en
4. Project Improvements and To-Do list:
  - [x] Once we start logging user activity , use Variational AutoEncoder to vizualize their mouvements in a 2D latent space of features.
  - [x] Get the X-Y coordinates from the mentionned Visualisation  and turn the problem into an irreguler Time-series forecasting problem
  - [x] For each user , assign a Reinforcement Learning Agent , the Agent's job is to learn the user's behaviour and predict 

using non Copyright music:
  ![Youtube Genres](https://user-images.githubusercontent.com/75742617/174759841-f7704546-0930-405d-85ae-dd4365c565ae.png)<br>
  
Project Architecture :view this svg in Light mode (green means accomplished , red means there's a problem we're figuring out , orange means we have solution/lacka  certain ressource btu gotta sit down and do it):
![image](https://user-images.githubusercontent.com/75742617/174777935-31d9a151-2d99-4442-b5e4-0f333b98d73f.png)
![image](https://user-images.githubusercontent.com/75742617/174778045-135a0c5e-6234-4926-bfe1-269370cfb99c.png)

 dealing with unbalanced data in the CNN's training:
![Stratified Kfold CV](https://user-images.githubusercontent.com/75742617/174760071-83182486-fc0d-4061-bc5d-dabcc14bf3b4.png)<br>
the CNN's architecture
![Music Genre Classification](https://user-images.githubusercontent.com/75742617/174760106-3055356d-063b-4a9d-9e23-4827464aa42c.svg)<br>
Scraped data distribution :
![Sample Distribution](https://user-images.githubusercontent.com/75742617/174760195-78dbdfe6-934b-4a12-962f-4162bd42dc1d.png)<br>
Seperation example (vocali.se) :
![Audio seperation Folder structure](https://user-images.githubusercontent.com/75742617/174760224-8bad4789-56e1-4cdd-be56-729999189539.png)<br>
