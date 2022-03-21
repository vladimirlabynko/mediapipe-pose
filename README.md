# mediapipe-pose

1)Install python 3.8 and create virtual environment using conda 
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
After installation in terminal enter 

```
conda create -n "name of env" python=3.8
conda activate "name of env" 
conda install -c anaconda pip
```
2) Install libraries 
go to project folder and enter in terminal
```
pip -r requirements.txt
```

3) run project 
```
python pose.py --input=/path/to/original/file --output=/path/to/output/processed/file
```
Wait until program print "Done!"
