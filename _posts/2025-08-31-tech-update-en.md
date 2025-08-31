# 🛠️ 2025-08-31 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Finer-Grained Control Over Container Restarts
The blog post discusses the new alpha feature introduced in Kubernetes v1.34, called "Container Restart Policy and Rules." This feature allows more granular control over container restarts within a Pod by enabling users to set individual restart policies for each container, overriding the Pod's global restart policy. It also allows conditional restarts based on the exit codes of individual containers. The feature addresses the limitations of a single Pod-level restart policy, which previously applied the same policy to all containers. The post provides examples and use cases, such as in-place restarts for training jobs, try-once init containers, and Pods with multiple containers having different restart requirements. To use this feature, the "ContainerRestartRules" feature gate must be enabled in Kubernetes 1.34+. The blog encourages feedback from users and involvement in the development process through the SIG Node community.
👉 [Read more](https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/)

## 🔹 Spring Boot - A Bootiful Podcast: JobRunr founder Ronald Dehuysser on what's new in version 8
The blog post is a podcast episode where the host talks with Ronald Dehuysser, the founder of JobRunr, about the new features and updates in JobRunr version 8.0.0. This discussion follows the SpringOne 2025 event. The post encourages readers to learn more about the latest release of JobRunr by visiting the provided link.
👉 [Read more](https://spring.io/blog/2025/08/28/a-bootiful-podcast-ronald-dehuysser)

## 🔹 Docker - Broadcom’s New Bitnami Restrictions? Migrate Easily with Docker
The blog post discusses recent restrictions imposed by Broadcom on Bitnami, a platform that has been instrumental in helping developers and operators deploy popular applications using prebuilt container images and Helm charts. Bitnami has been widely appreciated for standardizing installation and updates for various applications like WordPress and PostgreSQL. The post suggests using Docker as an alternative for those affected by these new restrictions, highlighting the ease of migration with Docker. The article also acknowledges Bitnami's contributions to the open-source and cloud-native community.
👉 [Read more](https://www.docker.com/blog/broadcoms-new-bitnami-restrictions-migrate-easily-with-docker/)

## 🔹 Java - The Java Platform Extension is now also available on open-vsx.org
The blog post announces that the new Java Platform Extension for Visual Studio Code is now available on open-vsx.org, a marketplace for open-source extensions. This update enhances the Java development experience in VS Code by providing improved features and accessibility for developers. The extension aims to streamline Java coding workflows and broaden its reach by being accessible on this additional platform.
👉 [Read more](https://inside.java/2025/08/29/java-vscode-extension-update/)

## 🔹 Golang - Testing Time (and other asynchronicities)
The blog post titled "Testing Time (and other asynchronicities)" delves into the challenges and methodologies associated with testing asynchronous code. It specifically explores the use of the `testing/synctest` package, which provides tools for effectively managing and testing asynchronous operations. The content is based on insights and discussions from a talk presented at GopherCon Europe 2025, sharing practical advice and techniques for developers working with asynchronous processes in Go.
👉 [Read more](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They are excited to discuss the upcoming release of Helm 4 and invite attendees to engage with their maintainers during talk sessions and visit their booth in the Project Pavilion. The post promises more details on Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

