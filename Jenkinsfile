node {
    stage('Clone repository') {
           checkout changelog: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/lenats03/WoG.git']]]
    }
    stage('Build image') {

            bat "docker-compose build"
    }
    stage ('Run container'){
            bat "docker-compose --project-name wog_score_for_test up -d  --force-recreate"
            bat "docker ps"
            /* Run some tests which require MySQL */
    }
    stage('test'){
            bat 'docker cp  ./scores.txt wog_score_for_test:/app/'
            bat 'C:/Users/Lenats/AppData/Local/Programs/Python/Python38/python.exe "C:/Users/Lenats/PycharmProjects/WorldOfGames/tests/e2e.py"'
    }
    stage ('kill container'){
            bat "docker kill wog_score_for_test"
    }
	stage('Push') {
            withDockerRegistry(credentialsId: 'dokcerhub_lenats', url: '') {
                 bat "docker push lenats/wog:$build_id"
            }

    }

}