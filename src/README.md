
# Creating the dataset


## Scraping the names
The names of the actors/actresses whose quotes were publicly avalibale were scraped.

    python scrape_names.py > names.txt

## Gathering Images
The links for the images of these 267 artists were fetched using the Bing Image Search API.
A free tier version was used.
These images were saved into *Actors Images.csv*

    python get_images.py
  
  ## Deep Learning model
  A BERT based deep learning model was built.
  
  This transfer learning based model was trained upon text and personality traits data obtained from various research papers (check references section).

     python create_traits_dataset.py

  
  See *BERT/Copy_of_Finetuning_BERT_with_Keras_and_tf_Module.ipynb* for training and hyperparameter details.
  
  The model was saved for inference
  
## Scraping Quotes
The quotes of the artists were scraped and a dataset was made for inference.

    python scrape_quotes.py
 
 ## Infernece
 The quotes were put throught the saved model to get the personality traits of the artists.
 See *BERT/Copy_of_Finetuning_BERT_with_Keras_and_tf_Module.ipynb* for inference details.
  
## References
 - Notebook:
   https://colab.research.google.com/drive/1ofSfThTBlWjOx5dqXmdsIol-MdiqCyZC#scrollTo=zZXDHbHd7eCx
 - Quotes and Names: brainyquote.com
 - Research: https://github.com/ichenjia/personality-detection
