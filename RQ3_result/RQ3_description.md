#### Description ####

This folder presents the result of RQ3, i.e., we investigate the effects of mutation type, mutation order, and mutation position on the mutant generation. We adopt the output distance to evaluate different mutants.

We select four DL models, i.e., deeplabv3, ssimae, vgg16, openpose to carry out the ``mutation position'' experiments as shown in four csv files. The first column shows the mutation type, the second column shows the mutation iterations, the third to fifth columns show the output distances of the generated mutants across different DL frameworks of Mindspore, PyTorch, and ONNX. Please note that the left value in the brackets from the third to fifth columns represents the output distance generated by mutating middle layers in backbone of the model, while the right value represents the the output distance generated by mutating middle layers in task head of the model. The txt file in mutation_log folder records the mutation log of each round. Every two mutations are separated by blank lines, and we record the name of the middle layer of the mutation, mutation result, mutation type, and other necessary parameters.

The mutation_type/mutation_order folder shows the experiment resulst of mutation type and mutation position. The result of 14 mutation operators are shown in the 14 csv files. The mixed mutation (mutating with mulptile mutation operators) result is shown the group csv file. The first column represents the model name, the second column shows the mutation rounds, the third to fifth column shows the output distance of generated mutants across different DL frameworks of Mindspore, PyTorch, and ONNX. The single_mutation_log and the group_mutation_log stores the file that record the mutation log of the each mutation operator and mulptile mutation operators separately. The first column of these CSV files in two folders record the type of each mutation, the second column records the name of the middle layer of the mutation (if the mutation fails, record "no"), and the third column records the mutation result.


