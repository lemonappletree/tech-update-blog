# 🛠️ 2025-09-20 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Recovery From Volume Expansion Failure (GA)
The blog post discusses the general availability of a new feature in Kubernetes v1.34, which allows automated recovery from volume expansion failures. This feature addresses issues like typos when expanding persistent volumes, which was previously a challenging problem to resolve. With the new update, users can reduce the requested size of a PersistentVolumeClaim (PVC) if the expansion hasn't completed, enabling Kubernetes to automatically correct it. This update eliminates the need for tedious manual recovery by cluster admins and returns any consumed quota from failed expansions.

The post explains how users can correct expansion mistakes and outlines the conditions under which recovery is possible. It also highlights improved error handling and observability, with new API fields for monitoring the expansion process. The update fixes longstanding bugs in resizing workflows and provides better error reporting for failed expansions. The development of this feature was supported by contributions and feedback from several Kubernetes community members.
👉 [Read more](https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/)

## 🔹 Spring Boot - Spring Modulith 2.0 M3 released
The blog post announces the release of Spring Modulith 2.0 M3, highlighting several new features. These include an updated event publication repository implementation for JPA, support for serialized event publication externalization, and Jackson 3 support for event publication serialization and externalization. The release also offers more lenient verification for Hexagonal Architecture, an upgrade to Spring Boot 4.0 M3, and an upgrade to jMolecules 2025 RC5. Further details can be found in the full changelog linked in the post.
👉 [Read more](https://spring.io/blog/2025/09/19/spring-modulith-2-0-m3-released)

## 🔹 Docker - Silent Component Updates & Redesigned Update Experience
The blog post discusses the new improvements in Docker Desktop 4.46, focusing on automatic component updates and a redesigned update experience. These changes aim to streamline the update process, ensuring that development tools remain current without disrupting user productivity. The automatic updates will keep components up-to-date silently in the background, enhancing user experience by minimizing interruptions.
👉 [Read more](https://www.docker.com/blog/docker-desktop-silent-component-updates/)

## 🔹 Java - JEP targeted to JDK 26: 504: Remove the Applet API
The blog post discusses JEP 504, which is aimed at removing the Applet API in JDK 26. The Applet API has been largely obsolete for years, with modern web technologies offering better alternatives. The removal is part of a broader effort to streamline the Java platform by eliminating outdated and seldom-used features. This change is targeted for inclusion in JDK 26, marking a significant step in the ongoing evolution of Java. The blog provides insights into the reasons for this removal and its implications for developers.
👉 [Read more](https://inside.java/2025/09/19/jep504-target-jdk26/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
The blog post announces a survey for Go programming language users, aiming to gather feedback on their experiences with Go. The purpose of the survey is to help shape the future development of the language by understanding the community's needs and challenges. The post encourages Go users to participate in the survey and contribute to the language's evolution.
👉 [Read more](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, indicating that the development of Helm v4 is nearing completion. It provides insights into ongoing developments and encourages the broader community to participate and contribute to the process. The post likely outlines key features and changes in the new version, as well as ways for community members to get involved in testing and feedback.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

