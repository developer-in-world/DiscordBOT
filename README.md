# DiscordBOT
## How to Clone This GitHub Project

This README provides instructions on how to clone this GitHub project to your local machine.

**Prerequisites:**

* Git installed on your local machine
* A command prompt or terminal

**Cloning the Project:**

There are two main methods for cloning the project:

**1. Using HTTPS URL:**

1. **Open the project page on GitHub.**
2. Click the **Code** button and copy the **HTTPS URL**.
3. Open a **command prompt** or **terminal** on your local machine.
4. Navigate to the directory where you want to clone the project.
5. Run the following command, replacing `<URL>` with the copied HTTPS URL:

```
git clone <https://github.com/developer-in-world/DiscordBOT.git>
```

This command will download the project files to your local machine and create a new directory for the project.

**2. Using SSH URL:**

1. **Open the project page on GitHub.**
2. Click the **Code** button and choose the **SSH** option.
3. Copy the displayed **SSH URL**.
4. Open a **command prompt** or **terminal** on your local machine.
5. Navigate to the directory where you want to clone the project.
6. Run the following command, replacing `<URL>` with the copied SSH URL:

```
git clone <git@github.com:developer-in-world/DiscordBOT.git>
```

This command will download the project files to your local machine and create a new directory for the project.

**Additional Notes:**

* If the project is private, you will need to be logged in to your GitHub account before you can clone it.
* You can specify a specific branch or commit to download using the `-b` or `-c` flags with the `git clone` command.
* For more information on using Git, you can refer to the official Git documentation: [https://git-scm.com/](https://git-scm.com/)

**After Cloning:**

Once you have cloned the project, you can access and use it like any other project on your local machine. You can use your preferred code editor or IDE to open and modify the files, and you can run any scripts or programs that are included in the project.

**Contributing to the Project:**

If you would like to contribute to this project, you can fork the repository and create a pull request. Please refer to the project's contribution guidelines for more information.

**Happy coding!**

## DicordBOT
This repository contains the code for a basic Discord bot that utilizes Natural Language Processing (NLP) to provide responses to user messages. The bot hides its Discord token using environment variables for security and leverages the `dotenv` library for easy configuration.

**Features:**

- Leverages `discord.py` for interaction with the Discord API.
- Utilizes the `response` module (assumed to be in a separate file) for NLP-based response generation.
- Handles private messages (starting with "?") and public messages in channels.
- Prints received messages and corresponding responses to the console for logging purposes.

**Installation:**

1. **Create a `.env` file:**

   - Create a file named `.env` in the project's root directory.
   - Add the following line to the `.env` file, replacing `<your-token>` with your actual Discord bot token:

     ```
     DISCORD_TOKEN=<your-token>
     ```

   **Important:** Never commit the `.env` file to version control, as it contains sensitive information, I forgot to do it so, I had to reset the API code.

2. **Install dependencies:**

   - Navigate to the project directory in your terminal.
   - Run the following command to install required libraries:

     ```bash
     pip install discord python-dotenv
     ```

**Usage:**

1. **Start the bot:**

   - Make sure your `.env` file is properly configured.
   - Run the script using the following command:

     ```bash
     python main.py
     ```

   This will start the bot and log received messages and responses to the console.

**Testing:**

- Invite your bot to a Discord server using the Discord Developer Portal.
- Send messages to the bot, both publicly in channels and privately using direct messages starting with "?".
- Observe the console output to verify the bot receives and responds to messages.

**Further Development:**

- Enhance the NLP capabilities of the `response` module by integrating with NLP libraries like NLTK or spaCy.
- Implement additional features like user authentication, command handling, or game integration.
- Explore advanced Discord functionalities provided by the `discord.py` library.


**Additional Notes:**

- Remember to replace `<your-username>` in the cloning command with your actual GitHub username.
- Ensure that you have Python and `pip` (the package installer) installed on your system.
