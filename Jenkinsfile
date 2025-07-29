pipeline {
    agent { label 'master' }

    stages {
        stage('Build on Host') {
            steps {
                sshagent(['host-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no user@host "cd /home/yogatom/docker-tutorial/redis-web && docker-compose down && docker-compose build && docker-compose up -d"
                    '''
                }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YogaTom/redis-web.git'
            }
        }

        stage('Build with Docker Compose') {
            steps {
                sh '''
                    docker-compose down
                    docker-compose build
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker-compose up -d
                    # 可以根据你的项目情况修改，比如用 curl 检查健康
                    sleep 5
                    docker-compose ps
                '''
            }
        }

        stage('Stop Services') {
            steps {
                sh 'docker-compose down'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
        }
    }
}

