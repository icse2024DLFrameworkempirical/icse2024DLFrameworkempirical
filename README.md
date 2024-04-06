### Deep Learning Framework Testing via Model Mutation: How Far Are We?

This is the open repository of our ICSE 2025 paper:  Deep Learning Framework Testing via Model Mutation: How Far Are We?

#### Description ####

In this work, we carry out two types of research work: (1) construct a high-priority framework defect classification based on the expertise of developers;（2）conduct a large-scale empirical study on 4 state-of-the-art mutation-based testing methods.

For the first type of work, we collect the issue reports from three framework communities, i.e., MindSpore, PyTorch, and TensorFlow. Then we filter those high-priority framework defects based on the tags labeled by developers. Finally, we recurit six volunteers to label the high-priority framework defects. The labeled results can be found in the folder ``RQ1_result''.

For the second type of work, we  run 4 existing methods on the latest releases of four popular DL frameworks: PyTorch, MindSpore, ONNX, and TensorFlow with a total of 23 classic DL models from 8 scenario tasks. Besides, to analyze the impact factors of model mutation in existing methods, we also collect 14 mutation operators including 4 types, i.e., structure-mutation, input-mutation, weight-mutation, and parameter-mutation. We analyze the detects detected by existing methods from (1) our study and (2) previous studies. The defects detected in our study can be found in the 'defects.xlsx' file. Among them, the first column is the description of the content of the issue, the second column is whether the issue has been confirmed by the framework developer, the third column is whether the issue has been fixed, the fourth column is the label of the issue, the fifth column is the type of issue (divided into inconsistent defects, NAN defects, and Crash defects based on previous work types), and the last column is the framework category to which the issue report belongs.

Besides, to investigate the impact factors that affect model mutation, i.e., mutation type, mutation position (the middle layers selected to mutate), and mutation order. We compare the output inconsistency of the mutants generated by different experiments. The results can be found in the folder ``RQ3_result'.'

If you have any questions, please leave a message here to contact us. The following explains the organizational structure of the result files on this repository.

