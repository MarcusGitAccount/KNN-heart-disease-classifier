#### Description

Writing from scratch a classifier to predict heart diseases using knn.

#### Dataset:

http://archive.ics.uci.edu/ml/datasets/Heart+Disease

#### Algorithm: 

K nearest neighbours using ball trees.

### Data provided by

1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation:
Robert Detrano, M.D., Ph.D.

### Data Attribute Information:

1. **#3**  (age)       
2. **#4**  (sex)       
3. **#9**  (cp)        
4. **#10** (trestbps)  
5. **#12** (chol)      
6. **#16** (fbs)       
7. **#19** (restecg)   
8. **#32** (thalach)   
9. **#38** (exang)     
10. **#40** (oldpeak)   
11. **#41** (slope)     
12. **#44** (ca)        
13. **#51** (thal)      
14. **#58** (num)       (the predicted attribute)

**9** cp: chest pain type
  -- Value 1: typical angina
  -- Value 2: atypical angina
  -- Value 3: non-anginal pain
  -- Value 4: asymptomatic

**10** trestbps: resting blood pressure (in mm Hg on admission to the 
hospital)

**12** chol: serum cholestoral in mg/dl

**16** fbs: (fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)

**19** restecg: resting electrocardiographic results
  -- Value 0: normal
  -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST 
              elevation or depression of > 0.05 mV)
  -- Value 2: showing probable or definite left ventricular hypertrophy
              by Estes' criteria

**32** thalach: maximum heart rate achieved

**38** exang: exercise induced angina (1 = yes; 0 = no)

**40** oldpeak = ST depression induced by exercise relative to rest

**41** slope: the slope of the peak exercise ST segment
  -- Value 1: upsloping
  -- Value 2: flat
  -- Value 3: downsloping
**44** ca: number of major vessels (0-3) colored by flourosopy

**51** thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

**58** num: diagnosis of heart disease (angiographic disease status)
  -- Value 0: < 50% diameter narrowing
  -- Value 1: > 50% diameter narrowing
  (in any major vessel: attributes 59 through 68 are vessels)

#### Performance(accuracy):

Currently only 7