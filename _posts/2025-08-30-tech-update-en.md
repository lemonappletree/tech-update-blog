# 🛠️ 2025-08-30 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Finer-Grained Control Over Container Restarts
The tech blog post discusses the release of Kubernetes v1.34, which introduces an alpha feature called "Container Restart Policy and Rules." This feature allows users to set individual restart policies for each container within a Pod, offering more granular control compared to the previous Pod-level restart policy. Users can also define rules to conditionally restart containers based on exit codes. This feature addresses limitations of the single restart policy by enabling scenarios such as in-place restarts for training jobs, try-once init containers, and Pods with multiple containers having different restart requirements. To use this feature, users need to enable the `ContainerRestartRules` feature gate on Kubernetes 1.34+. The post encourages feedback and participation from the community, providing several ways to engage with the Kubernetes SIG Node team.
👉 [Read more](https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/)

## 🔹 Spring Boot - A Bootiful Podcast: JobRunr founder Ronald Dehuysser on what's new in version 8
The blog post is a summary of a podcast episode where the host talks with Ronald Dehuysser, the founder of JobRunr, about the latest updates in JobRunr version 8.0.0. The conversation takes place shortly after the SpringOne 2025 event, and the post includes a link for readers to learn more about the new release of JobRunr.
👉 [Read more](https://spring.io/blog/2025/08/28/a-bootiful-podcast-ronald-dehuysser)

## 🔹 Docker - Boost Your Copilot with SonarQube via Docker MCP Toolkit and Gateway
The blog post discusses the integration of SonarQube with AI copilots and code generation tools using the Docker MCP Toolkit and Gateway. As AI tools boost productivity, they also increase the risk of insecure or untested code entering production. SonarQube is highlighted as a widely adopted solution to mitigate these risks. It offers a comprehensive set of features to identify and address vulnerabilities, bugs, and poor coding practices, ensuring that code quality remains high even as automation and AI tools are increasingly used in the development process.
👉 [Read more](https://www.docker.com/blog/blog-sonarqube-copilot-docker-mcp-toolkit/)

## 🔹 Java - The Java Platform Extension is now also available on open-vsx.org
The tech blog post announces that the Java Platform Extension for Visual Studio Code is now available on open-vsx.org. This release provides developers with an additional platform to access and utilize the extension, enhancing their Java development experience in VS Code. The update aims to improve accessibility and support for Java developers using alternative extension marketplaces.
👉 [Read more](https://inside.java/2025/08/29/java-vscode-extension-update/)

## 🔹 Golang - Testing Time (and other asynchronicities)
The blog post titled "Testing Time (and other asynchronicities)" focuses on the challenges and techniques involved in testing asynchronous code. It delves into the use of the `testing/synctest` package, which is designed to aid in testing such code effectively. The discussion is based on insights from a talk at GopherCon Europe 2025, providing readers with practical approaches and tools to handle the complexities of asynchronous operations in programming.
👉 [Read more](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. Helm 4 is currently in development and expected to be released later this year. Attendees are encouraged to engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides further details on Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

