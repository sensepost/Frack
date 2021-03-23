# Downloading and compiling orc-tools and setting up environment.

First download the latest orc-tools from https://orc.apache.org/docs/releases.html.

```
sudo apt-get install cmake mvn maven
tar -xvf orc-1.6.7.tar.gz
cd orc-1.6.7/
mkdir build
cd build
cmake ..
make package test-out
cp tools/src/csv-import /your_Frack_dir
```
If you copy csv-import to another directory that does not contain Frack.py, edit this to reflect this.

![Image011](media/Image_011.png)

If you copy csv_import to the same directory as Frack.py, you can skip above step.
Next go to your Frack directory, and run:
`pip3 install -r requirements.txt`

That’s it. Now you’ve got the ORC component you need, and your python3 requirements have been installed.

[Step2 - Configuring your Cloud infrastructure](media/Step2.md)
