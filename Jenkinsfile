pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        echo 'Running build automation'
        python3.7 Pytest.py
      }
    }
  }
}
