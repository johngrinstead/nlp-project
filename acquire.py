"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import pandas as pd
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = [
    "microsoft/AirSim", #1
    "microsoft/vcpkg", #2
    "microsoft/vscode-cmake-tools", #3
    "microsoft/CCF", #4
    "microsoft/beachball", #5
    "microsoft/vscode", #6
    "microsoft/playwright-python", #7
    "microsoft/TypeScript", #8
    "microsoft/covid-vaccine-bot", #9
    "microsoft/playwright-java", #10
    "microsoft/code-with-engineering-playbook", #11
    "microsoft/azure_arc", #12
    "microsoft/healthcare-shared-components", #13
    "microsoft/fluentui", #14
    "microsoft/just", #15
    "microsoft/winget-pkgs", #16
    "microsoft/llvm-mctoll", #17
    "microsoft/BotBuilder-Samples", #18
    "microsoft/Web-Dev-For-Beginners", #19
    "microsoft/winget-cli", #20
    "microsoft/playwright", #21
    "microsoft/botbuilder-tools", #22
    "microsoft/botbuilder-js", #23
    "microsoft/snmalloc", #24
    "microsoft/fundraising-and-engagement", #25
    "microsoft/KeyVaultScannerUtility", #26
    "microsoft/binskim", #27
    "microsoft/react-native-windows", #28
    "microsoft/InnerEye-DeepLearning", #29
    "microsoft/fast", #30
    "microsoft/onefuzz", #31
    "microsoft/pxt-jacdac", #32
    "microsoft/azure-pipelines-agent", #33
    "microsoft/ComplianceCxE", #34
    "microsoft/azure-maven-plugins", #35
    "microsoft/WebTemplateStudio", #36
    "microsoft/MentalHealthPlatform", #37
    "microsoft/OMEX-Azure-DevOps-Extensions", #38
    "microsoft/2LCS", #39
    "microsoft/PowerToys", #40
    "microsoft/azure-tools-for-java", #41
    "microsoft/DataCenterBridging", #42
    "microsoft/Recurring-Integrations-Scheduler", #43
    "microsoft/InnerEye-Gateway", #44
    "microsoft/OpticSim.jl", #45
    "microsoft/P.808", #46
    "microsoft/MixedRealityToolkit-Unity", #47
    "microsoft/vnet-in-azure-spring-cloud", #48
    "microsoft/BotFramework-Composer", #49
    "microsoft/vscode-react-native", #50
    "microsoft/appcenter-sdk-dotnet", #51
    "microsoft/playwright-sharp", #52
    "microsoft/microsoft-ui-xaml", #53
    "microsoft/checkedc", #54
    "microsoft/ai.ed", #55
    "microsoft/WPF-Samples", #56
    "microsoft/terminal", #57
    "TailwindTraders-Website", #58
    "webpack-bundle-compare", #59
    "microsoft/ALAppExtensions" #60
]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)
    
####################################################################################################################

def acquire_microsoft():
    '''
    This is a simple function to acquire the microsoft github scraped data by calling the cached data
    '''
    
    # call csv
    df = pd.read_csv('microsoft_github.csv')
    
    # remove unnamed column
    df = df.drop(columns = ['Unnamed: 0'])
    
    # remove nulls
    df.dropna(inplace=True)
    
    # make boolean variable for is or is not Typescript
    df['is_TypeScript'] = df.language == 'TypeScript'
    
    return df

