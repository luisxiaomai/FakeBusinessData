# FakeData
FakeData is a Python package that generates realistic business data, then run an associated jmeter case, thousands of data will be added to Project.

For the long term purpose, I hope the data is from Internet and user can create fake datasets for their data science/machine learning projects.

## Contents
1. [Requirements](#requirements)
1. [Installation](#installation)
1. [Usage](#usage)
1. [Localization](#localization)
1. [FAQ](#faq)
1. [Road Map](#road-map)

## Requirements

[Python 2.7](https://www.python.org/downloads/) need be installed

## Installation

```bash	
python setup.py install
```

## Usage

> **Generate fake data**

Just run ``csvfaker `` command to generate default fake data if you do not have any requiremnt for big volumes.

 ```bash
 csvfaker
 ```
 
Or if you want to generate hundreds of data you can run below command:

 ```bash
 csvfaker --bo_pairs customer=1000,product=1000,contactPerson=500,lead=100,targetGroup=20,campaign=10,warehouse=25,salesOrder=1000,goodReceipt=500,salesOpportunity=500 
 ```
 
> **Run jmeter case to add fake data to Your project**

**Precondition:**
-
-
-

Once basic data are generated, you can run the ``YourJmeterCase.jmx`` to import all the data to your project. 

## Localization

Command ``csvfaker`` can take a locale as an argument to return localized data. If no locale provided, the faker falls back to the
default en\_US locale.

If you want to Chinese data, just run 

 ```bash
 csvfaker -l zh_CN
 ```
 
## FAQ

### Why some requests will be failed becasue of "server not respond" or "socket connection Exception" when I run the jmeter case?

This may be related to which jmeter vesion you used and which http client you give to jmeter case. Recommend that using [Jmeter 3.1](https://archive.apache.org/dist/jmeter/binaries/) and set jmeter.httpsampler to HttpClient3.1. But if you use other version of jmeter and httpClient, you can refer to this [solution](https://stackoverflow.com/questions/25132655/the-target-server-failed-to-respond-jmeter)

## Road Map

- Business data will be captured by crawler
- Business data can be persisted into database for data science/machine learning purpose.
