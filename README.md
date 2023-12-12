#  Real-time Build Updates: Jenkins-to-Teams Notifications

Automating Jenkins to update build results in a customized format on Teams fosters collaboration and enhances team awareness within the development workflow.

## Introduction:

This Python and Robot Framework automation project brings together the power of Jenkins and Microsoft Teams seamlessly. The project's core revolves around establishing a robust connection between Jenkins and Teams, enhancing communication and transparency across the Continuous Integration and Continuous Deployment pipelines. A structured result template has been meticulously crafted by parsing the build XML file, enabling the smooth transmission of essential updates through a webhook directly into Microsoft Teams. This integration orchestrates real-time notifications, ensuring that teams stay in the loop with instant updates delivered straight to their collaborative workspace. By streamlining these updates, the project optimizes team communication, fostering efficiency, and a deeper level of transparency throughout the development lifecycle

## Steps Performed:

 - Write teams notification python code and integrate with robot framework for automation.
 - Generate webhook for perticular channel for build updates.
 - Create an EC2 Instance + Jenkins
 - Push Code on Github account.
 - Create a Jenkins pipeline for k8s cluster commission and decommission.
 - Get update Jenkins build to Teams channel such as 'post' section allows you to define actions that should be taken after a pipeline stage or the entire pipeline completes execution.

## Screenshots:

![gcp-commission](https://github.com/pranavp14/Jenkins-to-Teams-Notifications/assets/86883246/bcc0ed85-839c-46f6-9b09-97a19a83aa6e)
![aks-commission](https://github.com/pranavp14/Jenkins-to-Teams-Notifications/assets/86883246/6be69305-dfaa-4f9e-9adb-397cb8542978)
![aks-decommission](https://github.com/pranavp14/Jenkins-to-Teams-Notifications/assets/86883246/dbfc41db-1e7e-4c3b-bf56-a8719b0e10cf)
![Project-build](https://github.com/pranavp14/Jenkins-to-Teams-Notifications/assets/86883246/40354bb0-ec42-48db-9eb6-395ed1b4bf98)
