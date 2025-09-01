# 🛠️ 2025-09-01 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Finer-Grained Control Over Container Restarts
The blog post discusses the release of Kubernetes v1.34, which introduces an alpha feature called "Container Restart Policy and Rules." This feature allows users to set restart policies for individual containers within a Pod, as opposed to a single policy for the entire Pod. This change enables more control over container restarts, allowing conditions based on exit codes. Previously, the Pod-level restart policy limited the flexibility, but now different containers can have distinct restart behaviors. The post outlines several use cases, such as in-place restarts for AI/ML training jobs, "try-once" init containers, and Pods with multiple containers requiring different restart policies. To use this feature, the "ContainerRestartRules" feature gate must be enabled on a Kubernetes 1.34+ cluster. The blog provides examples of how to implement these new policies and encourages feedback from the community as the feature is still in the alpha stage.
👉 [Read more](https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/)

## 🔹 Spring Boot - A Bootiful Podcast: JobRunr founder Ronald Dehuysser on what's new in version 8
The blog post is a podcast episode summary where the host talks with Ronald Dehuysser, the founder of JobRunr, about the new features and updates in JobRunr version 8.0.0. The discussion follows the recent SpringOne 2025 event. For more detailed information on the updates, listeners are directed to visit the JobRunr blog linked in the post.
👉 [Read more](https://spring.io/blog/2025/08/28/a-bootiful-podcast-ronald-dehuysser)

## 🔹 Docker - Broadcom’s New Bitnami Restrictions? Migrate Easily with Docker
The blog post discusses Broadcom's new restrictions on Bitnami, a platform that has been crucial for developers and operators in deploying popular applications using prebuilt container images and Helm charts. Bitnami has helped standardize installation and updates for various applications like WordPress and PostgreSQL. The post highlights the importance of these services and suggests using Docker as an alternative for those affected by the new restrictions, emphasizing the ease of migration with Docker's tools and resources.
👉 [Read more](https://www.docker.com/blog/broadcoms-new-bitnami-restrictions-migrate-easily-with-docker/)

## 🔹 Java - All New Java Language Features Since Java 21 #RoadTo25
The blog post discusses the new language features introduced in Java 25, which focus on data-oriented programming, facilitating the entry of new developers, and enhancing Java's capabilities as a scripting language for automation. The author, Jose, explores these features to showcase how they improve Java's usability and functionality.
👉 [Read more](https://inside.java/2025/08/31/roadto25-java-language/)

## 🔹 Golang - Testing Time (and other asynchronicities)
The blog post titled "Testing Time (and other asynchronicities)" delves into the challenges of testing asynchronous code. It highlights the complexities involved in ensuring that asynchronous operations behave as expected and introduces the `testing/synctest` package as a solution to these challenges. The discussion is based on insights from a GopherCon Europe 2025 talk of the same title, providing a comprehensive exploration of effective strategies and tools for testing asynchronous processes in software development.
👉 [Read more](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They are excited to discuss the upcoming release of Helm 4. Attendees can join conversations with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion for more information on Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

