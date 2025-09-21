# 🛠️ 2025-09-21 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Recovery From Volume Expansion Failure (GA)
The blog post discusses the new general availability feature in Kubernetes v1.34 that allows automated recovery from persistent volume expansion failures. Previously, fixing such issues required manual intervention with cluster-admin access. With this update, users can now reduce the requested size of a PersistentVolumeClaim (PVC) if an error occurs, provided the expansion hasn't completed, allowing Kubernetes to automatically correct the size and return any consumed quota. The change also introduces improved error handling, observability, and fixes to long-standing bugs in the volume resizing workflows. The update is the result of extensive work and feedback from several contributors in the Kubernetes community.
👉 [Read more](https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/)

## 🔹 Spring Boot - Spring Modulith 2.0 M3 released
The blog post announces the release of Spring Modulith 2.0 M3, highlighting several new features. These include an updated event publication repository implementation for JPA, support for serialized event publication externalization, and Jackson 3 support for event publication serialization and externalization. It also introduces more lenient out-of-the-box verification for Hexagonal Architecture, upgrades to Spring Boot 4.0 M3, and jMolecules 2025 RC5. For further details, readers are directed to the full changelog.
👉 [Read more](https://spring.io/blog/2025/09/19/spring-modulith-2-0-m3-released)

## 🔹 Docker - Silent Component Updates & Redesigned Update Experience
The blog post discusses significant updates to Docker Desktop, aimed at enhancing user productivity. With the release of Docker Desktop 4.46, the platform introduces automatic component updates, allowing development tools to stay current without user intervention. Additionally, the update experience has been completely redesigned to prioritize user productivity. These changes are part of Docker's ongoing efforts to improve the update process for its users.
👉 [Read more](https://www.docker.com/blog/docker-desktop-silent-component-updates/)

## 🔹 Java - JEP targeted to JDK 26: 504: Remove the Applet API
The blog post discusses JEP 504, which is targeted for JDK 26 and involves the removal of the Applet API. The Applet API, once a common method for embedding interactive content in web browsers, has become obsolete due to advancements in web technologies and declining browser support. The removal of this API is part of a broader effort to clean up and streamline the Java Development Kit by eliminating outdated and unsupported features.
👉 [Read more](https://inside.java/2025/09/19/jep504-target-jdk26/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
The blog post announces a survey aimed at Go programming language users, inviting them to share their experiences and feedback. The goal of the survey is to gather insights that will help shape the future development and improvements of Go. The blog encourages all Go users to participate in the survey to contribute to the language's growth and evolution.
👉 [Read more](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
The blog post titled "Path To Releasing Helm v4" announces the release of the first Alpha version of Helm v4. It highlights that the development of Helm v4 is nearing completion and provides details on the current status of the project. The post also discusses opportunities for the broader community to get involved in the development and testing process as Helm v4 progresses towards its final release. For more information, readers are encouraged to visit the provided link.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

