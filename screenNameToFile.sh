#!/bin/bash
java -cp twitter4j-core-4.0.2.jar:.  MP.ProcessMp $1 | tee $1.txt
