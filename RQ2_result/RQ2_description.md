#### Description ####

This folder displays the results of running existing methods on the new framework version. We have chosen four existing methods: CRADLE, LEMON, AUDEE, and COMET. Due to the lack of source code provided by AUDEE, we only present the running results of the other three methods. The first column of the three CSV files displays the name of the model, the second column displays the number of mutation rounds, the third column displays the name of the mutation model, and the fourth column displays the output distance of the mutation model on the PyTorch and TensorFlow frameworks. Please note that we use ONNX, tf2ONNX, and ONNX2Torch conversion tools to convert the TensorFlow mutation model to the PyTorch framework for calculation. When this process fails, we record the output distance of the mutation model as -1. In addition, if the output distance is NAN, it will be displayed as empty in the CSV file.



