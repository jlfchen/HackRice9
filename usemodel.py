from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import os
import numpy as np
from matplotlib.image import imread
import pickle



def classify_photo(photo, gender):
    savedir = "/Users/matthewbrun/Fall 2019/HackRice9"
    pcafile = ["pca64modelfemale.p", "pca64modelmale.p"]
    kmeansfile = ["kmeanswomen.p", "kmeansmen.p"]
    os.chdir(savedir)
    pca = pickle.load(open(pcafile[gender],"rb"))
    kmeans = pickle.load(open(kmeansfile[gender],"rb"))
    npphoto = np.asarray(photo)
    npphoto = np.reshape(npphoto, (1,1536000))
    pcaphoto = pca.transform(npphoto)
    group = kmeans.predict(pcaphoto)
    return group

def similar_photos(group, gender):
    filedir = ["/Users/matthewbrun/Desktop/Tinder/Women", "/Users/matthewbrun/Desktop/Tinder/Men"]

