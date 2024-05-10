---
layout: ML_Project
permalink: /brain_age_project
feedformat: card
title: The brain age project (2020)
---
<br/>
*Joint with K.T. Dang, P. Klopfenstein, M. Masters, and J. Yeater, and advised by Prof. A.M. Selvitella (PFW).*

Our study aimed to find a new method for predicting the age of a subject from their brain biometrics (brain age problem). We utilized an isoperimetric-type ratio $ T^2/A $, where $ T $ is the membrane thickness and A is the surface area, for each region of the brain. This was done to create an explainable model and as a dimensionality reduction technique. We then trained a multivariable regression model on the ratios, but it failed to preserve the prediction accuracy of the multivariable regression model trained on the area and thickness data. Therefore, we tried other modeling techniques, utilizing a multinomial logistic model. When compared to the multinomial logistic model trained on the thickness and area data, the multinomial logistic model trained on the ratios preserved, and improved, prediction accuracy. Therefore, the isoperimetric-type ratios can be used as an explainable dimensionality reduction technique for modeling age using brain biometrics.