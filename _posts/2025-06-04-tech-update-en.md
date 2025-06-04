# 🛠️ 2025-06-04 Tech Update Summary

## 🔹 Kubernetes - Start Sidecar First: How To Avoid Snags
The blog post discusses strategies for ensuring that sidecar containers start before the main application in Kubernetes environments. With the Kubernetes v1.29.0 release, sidecar containers can be defined in the `.spec.initContainers` field, allowing them to start before the main app. However, this often results in simultaneous starts, which can be problematic if the main app depends on the sidecar. The post examines different approaches, such as using readiness and startup probes, to delay the main app's start until the sidecar is fully ready. It highlights the effectiveness of the `startupProbe` in achieving this delay and explores other options like the `postStart` lifecycle hook, though it requires custom logic. The findings are summarized in a table, emphasizing that while simultaneous starts are ideal, specific configurations can ensure the main app waits for the sidecar to be ready. The post provides guidance for deploying applications where the main app depends on a healthy sidecar.
👉 [Read more](https://kubernetes.io/blog/2025/06/03/start-sidecar-first/)

## 🔹 Spring Boot - This Week in Spring - June 3rd, 2025
The blog post "This Week in Spring - June 3rd, 2025" provides an update on recent activities and developments in the Spring community. The author shares their experience recording a session with IntelliJ IDEA project lead Aleksey Stukalov, highlighting new features for Java, Kotlin, and Spring developers. They express gratitude to the Jetbrains team and mention an upcoming speaking engagement at the JSpring conference. The post lists several new releases, including Spring Cloud 2022.0.11 (Kulburn), Spring Cloud 2025.0.0 (Northfields), and updates to Spring Cloud Gateway, addressing a security fix. It also recaps a recent podcast with Victor Rentea and mentions releases like Spring Modulith 1.4 and Vite Spring Boot 0.9.0. Additionally, the post discusses forthcoming IntelliJ IDEA features that support Spring Data AOT repositories and reverse engineering JPA entities, as well as anticipated Spring Modulith support. The full post can be accessed via a provided link.
👉 [Read more](https://spring.io/blog/2025/06/03/this-week-in-spring-june-3rd-2025)

## 🔹 Docker - How to Make an AI Chatbot from Scratch using Docker Model Runner
The blog post provides a detailed guide on creating a generative AI chatbot using Docker Model Runner. It highlights the challenges developers often encounter when building AI applications and explains how Docker Model Runner can address these issues. Additionally, the post includes a step-by-step tutorial on building the chatbot and discusses the use of observability tools like Prometheus, Grafana, and Jaeger to enhance the development process.
👉 [Read more](https://www.docker.com/blog/how-to-make-ai-chatbot-from-scratch/)

## 🔹 Java - What’s new for JFR in JDK 25
The blog post discusses the upcoming release of JDK 25, scheduled for September 16, which will feature three new Java Enhancement Proposals (JEPs) specifically for Java Flight Recorder (JFR). Additionally, there will be several improvements made to the `jdk.jfr` API and the `jfr` command. These updates aim to enhance the functionality and performance of JFR in the new version of the JDK.
👉 [Read more](https://inside.java/2025/06/03/new-jfr-jdk25/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
The blog post discusses the Go programming team's considerations regarding adding syntactic support for error handling in the Go programming language. It outlines the team's plans and deliberations on improving error handling mechanisms, weighing the benefits and potential drawbacks of introducing new syntax to enhance clarity and efficiency in managing errors. The post reflects the ongoing efforts to refine the language while maintaining its simplicity and effectiveness.
👉 [Read more](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team is attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They are working on Helm 4, which is expected to be released later this year. Attendees are encouraged to engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides more details on Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

