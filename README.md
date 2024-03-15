# Repository for "An abstract model for digital forensic analysis tools - A foundation for systematic error mitigation analysis"

This repository contains the dataset and additional materials for the paper:

"An abstract model for digital forensic analysis tools - A foundation for systematic error mitigation analysis" by Christopher Hargreaves, Alex Nelson, and Eoghan Casey, presented at DFRWS EU 2024 (https://dfrws.org/conferences/dfrws-eu-2024/, https://doi.org/10.1016/j.fsidi.2023.301679)

Abstract: As automation within digital forensic tools becomes more advanced there is a need for a systematic approach to ensure the validity, reliability, and standardization of digital forensic results. This paper argues for intermediate output in a standardized format within digital forensic tools to allow a methodical approach to tool validation that targets errors at each stage of processing. To achieve this, a detailed process model of digital forensic analysis tools is created, extrapolating the details of the internal processes performed by monolithic forensic tools. The research deconstructs the process flow within tools and presents an ‘abstract digital forensic tool’, revisiting earlier abstraction layer ideas. This not only identifies the interconnected processes within tools but allows discussion of the potential error that could be introduced at each stage, and how it could potentially propagate within a tool. A demonstration, with a dataset, is also included, structurally annotated using Cyber-investigation Analysis Standard Expression (CASE).

## Contents

This repository contains the discussed disk image that can result in some tools missing or inaccurately associating deleted files. 
Feel free to use it to test your tools. 
In an ideal world the tools would output the results in a standard representation, allowing automated comparison with the expected results. 

The script and files used for data generation are also included. For the corresponding CASE example, including expected output, please see https://github.com/casework/CASE-Examples/tree/master/examples/illustrations/partitions#partitions-examples 

## Citing

If you use the data please cite the original paper.

Hargreaves, C., Nelson, A. and Casey E, An abstract model for digital forensic analysis tools - A foundation for systematic error mitigation analysis, Forensic Science International: Digital Investigation. Vol. 48. Pages 301679. 2024. Selected Papers from the 11th Annual Digital Forensics Research Conference Europe (DFRWS EU 2024).



