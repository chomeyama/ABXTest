# ABXTest

## Simple explanation of this opensource

1. Create wav directory like the below example. Each set contains wav files and their file lists for the methods you want to compare. It's easier to understand if you actually browse the wav directory. The number of methods in each set does not have to match.

```
wav/
 |---- set1/
 |      |-- method1/
 |      |-- method1.list
 |
 |---- set2
 |      |-- method2/
 |      |-- method3/
 |      |-- method2.list
 |      |-- method3.list
 |
 |---- set3
 |      |-- method4/
 |      |-- method5/
 |      |-- method4.list
 |      |-- method5.list
 |
 ```
 The command ```find wav/set1 -name "*.wav" | grep "method1" > wav/set1/method1.list``` will be helpful to create list files.

2. Rewrite abx.js depending on the structure of the wav directory. In most cases, you only need to customize two parts from line 45 and 97.

3. Rewrite index.html as you like. Note that my email address is written as contact info, so you may have to change it to your own one.

4. Use Github Pages to deploy your own test. The test automatically emits a csv file when the test finishes.

If you want to conduct tests other than a ABX test, you need to modify the code significantly depending on the test.
You can utilize [MOSTest](https://github.com/chomeyama/MOSTest) if you want to conduct MOS test.

Please feel free to ask any questions you may have.
