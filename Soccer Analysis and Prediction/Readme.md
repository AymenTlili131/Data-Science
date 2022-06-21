0. Credits:
Please refer to this article/paper from which i got this free Dataset about soccer Events in 2017 and Cite them if you ever use their work : <br>
  A public data set of spatio-temporal match events in soccer competitions
Luca Pappalardo, Paolo Cintia, Alessio Rossi, Emanuele Massucco, Paolo Ferragina, Dino Pedreschi & Fosca Giannotti

Nature Scientific Data 6, Article number: 236 (2019)

if you use this code or the plots generated from it, please cite/mention the following papers:

Pappalardo, L., Cintia, P., Rossi, A. et al. A public data set of spatio-temporal match events in soccer competitions. Sci Data 6, 236 (2019) doi:10.1038/s41597-019-0247-7, https://www.nature.com/articles/s41597-019-0247-7
Pappalardo, L., Cintia, P., Ferragina, P., Massucco, E., Pedreschi, D., Giannotti, F. (2019) PlayeRank: Data-driven Performance Evaluation and Player Ranking in Soccer via a Machine Learning Approach. ACM Transactions on Intellingent Systems and Technologies 10(5) Article 59, DOI: https://doi.org/10.1145/3343172, https://dl.acm.org/citation.cfm?id=3343172
and the data collection on figshare:

Pappalardo, Luca; Massucco, Emanuele (2019): Soccer match event dataset. figshare. Collection. https://doi.org/10.6084/m9.figshare.c.4415000

1. Project Architecture:
  - Building a folder hierarchy
  - Extracting the data per match
    - Spatial data: Generate Heatmaps using Kernel distribution estimation
    - Temporal data: Time-series Acceleration and Invasion indices 
    - Social interaction :Passing network <-> Graph density and centrality measures
  - Building models
    - 1D conv for time-series + 3D conv for heatmaps  + cancat at conv output with 6 features from the Passing network
    - a model per team :train on the first 24 weeks of the season and test on the rest

2. Project Idea and motivation: 
  - Our Deep learning course professor assigned credits to making a project using any architecture of our choice
  - Everyone used CNNs in the context of computer vision and classification so I thought i'd go for regression instead
  - Initial idea was to work on predicting facial features after aging
  - I needed a dataset so I thought maybe get a cosmetic surgery or criminal/fugitive dataset but both have their shortcommings
  - I decided to work on something familer : "soccer" , it was UCL around that time but it wasn't my cup of tea to watch but the calculations made by gambling sites intrested me
  - looked up sites specific to this type of analysis and found this dataset in an article 
3. Project Technologies:
  - Pytorch, torchVision
4 .Project Improvements and To-Do list:
  - use Continual learning library Avalanche when transitionning between Game weeks
  - Use weight and biase to track the training process and Hardware usage

Example of Heatmaps : Event(Duel)
![image](https://user-images.githubusercontent.com/75742617/174775421-f2529a7d-ca96-4ddf-9afe-069a89f9a4a6.png)
<br>
Inavsaion Index :
![image](https://user-images.githubusercontent.com/75742617/174775509-4f90ba43-f2ae-4dd5-8965-e52d5c83bde8.png)
<br>
Acceleration Index :
![image](https://user-images.githubusercontent.com/75742617/174775557-247bd984-ad84-4bea-9511-c3540c5a7c32.png)
<br>
Passing network for both Teams ina  certain match :
![image](https://user-images.githubusercontent.com/75742617/174775732-944a8466-65ed-4927-86d9-eb3477fbdd2e.png)
<br>
Continual Learning : (a form of back propagation where we intentionally forget some of the weights in the previous Layers to allow for learning new patterns without node saturation)
![image](https://user-images.githubusercontent.com/75742617/174775970-16ca07a4-478c-47a2-b8df-499d3da59ab8.png)
<br>
The researcher asked experts for probability of scoring when in certain zones of the field:
![dangerousity](https://user-images.githubusercontent.com/75742617/174776109-832445b3-fb11-4215-a877-2dc5da3788a6.jpg)



