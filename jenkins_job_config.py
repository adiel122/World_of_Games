import xml.etree.ElementTree as ET

class JenkinsJobConfig:
    def __init__(self):
        self.job_config = """<project>
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.plugins.git.GitSCM" plugin="git@3.9.3">
    <configVersion>2</configVersion>
    <userRemoteConfigs>
      <hudson.plugins.git.UserRemoteConfig>
        <url>https://github.com/adiel122/World_of_Games.git</url>
      </hudson.plugins.git.UserRemoteConfig>
    </userRemoteConfigs>
    <branches>
      <hudson.plugins.git.BranchSpec>
        <name>*/main</name>
      </hudson.plugins.git.BranchSpec>
    </branches>
  </scm>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders>
    <hudson.tasks.Shell>
      <command>
        # Install the jenkins module
        pip3 install jenkins
        # Run the Python script
        python3 JenkinsRunner.py
      </command>
    </hudson.tasks.Shell>
  </builders>
  <publishers/>
  <buildWrappers/>
</project>
"""

    def get_config(self):
        return self.job_config

class JenkinsJobReader:
    def __init__(self, config):
        self.config = config

    def read_config(self):
        root = ET.fromstring(self.config)
        scm_url = root.find('.//hudson.plugins.git.UserRemoteConfig/url').text
        branch_name = root.find('.//hudson.plugins.git.BranchSpec/name').text
        build_command = root.find('.//hudson.tasks.Shell/command').text

        return {
            "scm_url": scm_url,
            "branch_name": branch_name,
            "build_command": build_command
        }
