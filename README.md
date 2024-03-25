### Deep Learning Framework Testing via Model Mutation: How Far Are We?

This is the implementation repository of our ICSE 2025 paper:  Deep Learning Framework Testing via Model Mutation: How Far Are We?

#### Description ####

In this work, we carried out two types of research work: (1) constructed a high-priority framework defect classification based on the expertise of developers;（2）conducted a large-scale empirical study on 4 state-of-the-art mutation-based testing methods.

collected 4 state-of-the-art mutation-based testing methods and 14 classic DL model mutation operators and collected a total of 11 classic DL models from 8 scenario tasks. 
We conducted empirical research on four popular DL frameworks: PyTorch, MindSpore, ONNX, and TensorFlow. Due to paper length limitations, 
we reported results that were not presented in the paper in this open-source repository. If you have any questions, please leave a message here to contact us. 
The following explains the organizational structure of the result files on this repository.


We report the framework defects detected during our experiments in the 'defects.xlsx' file. Among them, the first column is the description of the content of the issue, the second column is whether the issue has been confirmed by the framework developer, the third column is whether the issue has been fixed, the fourth column is the label of the issue, the fifth column is the type of issue (divided into inconsistent defects, NAN defects, and Crash defects based on previous work types), and the last column is the framework category to which the issue report belongs. Finally, we also draw corresponding images for the result files in the two folders "RQ1_Result" and "RQ2_Result", and the specific results can be found in the 'Figs' folder.



