pipeline {
    agent any

    stages {
        stage("cloning") {
            steps {
                git url: ' https://github.com/gowtham123K/nineth.git', branch: 'main'
            }
        }

        stage("dependency") {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install pytest
                '''
            }
        }

        stage("testing") {
            steps {
                bat '''
                call venv\\Scripts\\activate
                test_main.py
                '''
            }
        }
        stage("deploy"){
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    main.py
                    '''
            }
        }
    }
}
