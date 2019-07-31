pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        sudo echo 'Running build automation' > /home/test.tx
        sudo python3.7 python.py
      }
    }
  }
}
