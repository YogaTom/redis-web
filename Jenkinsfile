pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-ssh', url: 'git@github.com:YogaTom/redis-web.git'
            }
        }

        stage('Deploy to Remote') {
            steps {
                sshagent(credentials: ['deploy-alicloud']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no tom@8.138.221.221 "
                        if [ ! -d /home/tom/redis-web/.git ]; then
                            git clone git@github.com:YogaTom/redis-web.git /home/tom/redis-web
                        fi
                        cd /home/tom/redis-web
                        git pull
                        sudo docker compose down
                        sudo docker compose build
                        sudo docker compose up -d
                    "
                    '''
                }
            }
        }
    }
}

