# 🛠️ 2025-09-22 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Recovery From Volume Expansion Failure (GA)
The blog post discusses the new feature in Kubernetes v1.34 that allows automated recovery from volume expansion failures and has reached general availability. Previously, correcting mistakes like typos in persistent volume expansion required manual intervention and cluster-admin access, but now users can reduce the requested size of a PersistentVolumeClaim (PVC) if the expansion hasn't completed. This enables Kubernetes to automatically correct the size and return any consumed quota. The update also includes improved error handling and observability for volume expansions, introducing new API fields to monitor progress and error conditions. This feature addresses longstanding bugs and enhances the overall resizing workflow. The blog acknowledges contributors who helped achieve this improvement.
👉 [Read more](https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/)

## 🔹 Spring Boot - Spring Modulith 2.0 M3 released
The blog post announces the release of Spring Modulith 2.0 M3, highlighting several new features. These include an updated event publication repository implementation for JPA, support for serialized event publication externalization, and Jackson 3 support for event publication serialization. Additionally, there are enhancements for Hexagonal Architecture verification, and upgrades to Spring Boot 4.0 M3 and jMolecules 2025 RC5. More detailed information can be found in the full changelog linked in the post.
👉 [Read more](https://spring.io/blog/2025/09/19/spring-modulith-2-0-m3-released)

## 🔹 Docker - Silent Component Updates & Redesigned Update Experience
The blog post discusses a new feature in Docker Desktop 4.46 that introduces automatic component updates and a redesigned update experience. This initiative aims to enhance productivity by ensuring development tools remain up-to-date without interrupting the user's workflow. The update process is streamlined to operate silently in the background, minimizing disruptions and allowing users to focus on their work.
👉 [Read more](https://www.docker.com/blog/docker-desktop-silent-component-updates/)

## 🔹 Java - Paths to Support Additional Numeric Types on the Java Platform #JVMLS
The tech blog post titled "Paths to Support Additional Numeric Types on the Java Platform" discusses the potential for expanding the range of numeric types available in the Java platform. While Java's current set of numeric types has remained stable over the years, there is a growing demand for additional types, particularly for scientific, engineering, and machine learning applications. These fields can benefit from using linear algebra, complex numbers, and smaller numeric types like 16-bit and even 8-bit floating-point numbers, which are being considered by the IEEE SA Working Group P3109 for standardization. The talk addresses what is necessary to fully support these new numeric types in Java and explores the trade-offs involved in different approaches to implementing this support.
👉 [Read more](https://inside.java/2025/09/21/jvmls-java-additional-numeric-types/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
The blog post announces a survey aimed at gathering feedback from users of the Go programming language. The purpose of the survey is to understand how Go is performing for its users and to collect insights that will help shape the future development of the language. The post encourages Go users to participate in the survey and contribute their experiences and suggestions.
👉 [Read more](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
The first Alpha version of Helm v4 has been released, marking a significant milestone in its development. As Helm v4 approaches its final stages, the blog post provides details on the current progress and outlines how the community can participate in the release process. The post encourages community engagement to help shape the final version of Helm v4.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

