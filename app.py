{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyOwB3NGli/bs6aGHxgi3+/B",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Fatima-sab/CV/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "7NHQfM4oEShz",
        "outputId": "de8bc10a-b2df-4059-d633-5ee91e282323"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-81d01639d91a>\u001b[0m in \u001b[0;36m<cell line: 81>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     79\u001b[0m \u001b[0;31m# Create CV\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m \u001b[0mcv\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mCVBuilder\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 81\u001b[0;31m \u001b[0mcv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbuild_cv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     82\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     83\u001b[0m \u001b[0md\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-1-81d01639d91a>\u001b[0m in \u001b[0;36mbuild_cv\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     69\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     70\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mbuild_cv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 71\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_personal_details\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     72\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_education_details\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     73\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_work_experience\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-1-81d01639d91a>\u001b[0m in \u001b[0;36mget_personal_details\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mget_personal_details\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter your full name: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     13\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0memail\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter your email address: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0maddress\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter your address: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ],
      "source": [
        "class CVBuilder:\n",
        "    def __init__(self):\n",
        "        self.name = \"\"\n",
        "        self.email = \"\"\n",
        "        self.address = \"\"\n",
        "        self.education = {}\n",
        "        self.work_experience = []\n",
        "        self.skills = []\n",
        "        self.languages = []\n",
        "\n",
        "    def get_personal_details(self):\n",
        "        self.name = input(\"Enter your full name: \")\n",
        "        self.email = input(\"Enter your email address: \")\n",
        "        self.address = input(\"Enter your address: \")\n",
        "\n",
        "    def get_education_details(self):\n",
        "        print(\"\\nEnter your educational details:\")\n",
        "        for level in [\"High School\", \"Secondary School\", \"Bachelors\", \"Masters\"]:\n",
        "            school_name = input(f\"Enter the name of {level} institution: \")\n",
        "            year = input(f\"Enter the year of completion for {level}: \")\n",
        "            self.education[level] = {\"Institution\": school_name, \"Year\": year}\n",
        "\n",
        "    def get_work_experience(self):\n",
        "        print(\"\\nEnter your work experience (type 'done' when finished):\")\n",
        "        while True:\n",
        "            company = input(\"Company Name: \")\n",
        "            if company.lower() == \"done\":\n",
        "                break\n",
        "            role = input(\"Role/Position: \")\n",
        "            duration = input(\"Duration (e.g., Jan 2020 - Dec 2021): \")\n",
        "            self.work_experience.append({\"Company\": company, \"Role\": role, \"Duration\": duration})\n",
        "\n",
        "    def get_skills(self):\n",
        "        print(\"\\nEnter your soft skills (type 'done' when finished):\")\n",
        "        while True:\n",
        "            skill = input(\"Skill: \")\n",
        "            if skill.lower() == \"done\":\n",
        "                break\n",
        "            self.skills.append(skill)\n",
        "\n",
        "    def get_languages(self):\n",
        "        print(\"\\nEnter languages you know (type 'done' when finished):\")\n",
        "        while True:\n",
        "            language = input(\"Language: \")\n",
        "            if language.lower() == \"done\":\n",
        "                break\n",
        "            self.languages.append(language)\n",
        "\n",
        "    def display_cv(self):\n",
        "        print(\"\\n--- CV ---\\n\")\n",
        "        print(f\"Name: {self.name}\")\n",
        "        print(f\"Email: {self.email}\")\n",
        "        print(f\"Address: {self.address}\")\n",
        "        print(\"\\n--- Education ---\")\n",
        "        for level, details in self.education.items():\n",
        "            print(f\"{level}: {details['Institution']} ({details['Year']})\")\n",
        "\n",
        "        print(\"\\n--- Work Experience ---\")\n",
        "        for exp in self.work_experience:\n",
        "            print(f\"{exp['Role']} at {exp['Company']} ({exp['Duration']})\")\n",
        "\n",
        "        print(\"\\n--- Soft Skills ---\")\n",
        "        for skill in self.skills:\n",
        "            print(f\"- {skill}\")\n",
        "\n",
        "        print(\"\\n--- Languages ---\")\n",
        "        for language in self.languages:\n",
        "            print(f\"- {language}\")\n",
        "\n",
        "    def build_cv(self):\n",
        "        self.get_personal_details()\n",
        "        self.get_education_details()\n",
        "        self.get_work_experience()\n",
        "        self.get_skills()\n",
        "        self.get_languages()\n",
        "        self.display_cv()\n",
        "\n",
        "\n",
        "# Create CV\n",
        "cv = CVBuilder()\n",
        "cv.build_cv()\n",
        "\n",
        "d"
      ]
    }
  ]
}