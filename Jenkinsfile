node {
    def rc
    def image_c
    stage('Clone repository') {

            checkout scm
    }
    stage('Build image') {

            image_c = docker.build("wog:${env.BUILD_ID}")
    }
    stage ('Run and test')
    image_c.withRun(' -p 5001:8777') {c ->
        /* Wait until mysql service is up */
        docker.ps(){}
        cmd 'while ! wog ping -h0.0.0.0 --silent; do sleep 1; done'
        /* Run some tests which require MySQL */
        rc = cmd 'python "C:/Users/Lenats/PycharmProjects/WorldOfGames/tests/e2e.py"'
    }

}