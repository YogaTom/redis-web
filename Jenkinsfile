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
                sshagent(credentials: ['deploy-ssh']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no tom@8.138.221.221 << 'EOF'
                        cd /opt/redis-web || git clone git@github.com:YogaTom/redis-web.git /opt/redis-web
                        cd /opt/redis-web
                        git pull
                        sudo docker compose down
                        sudo docker compose build
                        sudo docker compose up -d
                    EOF
                    '''
                }
            }
        }
    }
}

