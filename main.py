import os
import re

#rootdir = '/var/lib/jenkins/jobs/cicd-jobs/jobs/incubator'

regex = '.*deployment-manual-dev/config.xml'

newstring = 'com.wangyin.parameter.WHideParameterDefinition'
oldstring = 'hudson.model.StringParameterDefinition'

def changePipeline(path):
    print(path)
    #read file
    with open(path,'r') as file:
        filedata = file.read()
    #replace the string
    filedata = filedata.replace(oldstring,newstring,2)
    #write file
    with open(path,'w') as file:
        file.write(filedata)

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if(re.match(regex,os.path.join(subdir,file))):
            #print(os.path.join(subdir,file))
            changePipeline(os.path.join(subdir,file))
