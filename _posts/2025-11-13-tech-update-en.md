# 🛠️ 2025-11-13 Tech Update Summary

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
The blog post announces the upcoming retirement of Ingress NGINX, a popular Ingress controller in the Kubernetes ecosystem. Kubernetes SIG Network and the Security Response Committee have decided to retire Ingress NGINX by March 2026, after which no further releases, bug fixes, or security updates will be provided. The decision is due to maintenance challenges and insufficient support, despite the controller's popularity and flexibility. Users are advised to migrate to alternatives, such as the Gateway API or other Ingress controllers listed in the Kubernetes documentation. Existing deployments of Ingress NGINX will continue to function, and installation artifacts will remain available. The blog also recognizes the contributions of Ingress NGINX maintainers and recommends that users start transitioning to other solutions immediately.
👉 [Read more](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Null-Safe applications with Spring Boot 4
The blog post discusses the integration of null-safety features in Spring Boot 4, as part of the ongoing efforts to enhance the Spring portfolio's robustness by addressing the "billion dollar mistake" of null references. The post highlights the use of JSpecify annotations to explicitly define nullability in Java codebases, which helps prevent `NullPointerExceptions` in production. The Spring team has made significant progress in making most of its APIs null-safe across various projects, including Spring Boot 4.0, Spring Framework 7.0, and others. The post also emphasizes the collaboration with JetBrains and the support provided by IntelliJ IDEA for JSpecify annotations. Developers are encouraged to upgrade to null-safe versions and use build-time nullability checkers like NullAway for greater safety. The blog concludes by encouraging more open-source libraries to adopt JSpecify, anticipating future benefits from potential JVM enhancements for null-restricted and nullable types.
👉 [Read more](https://spring.io/blog/2025/11/12/null-safe-applications-with-spring-boot-4)

## 🔹 Docker - Docker Desktop 4.50: Indispensable for Daily Development
The blog post discusses the significant advancements introduced in Docker Desktop 4.50, highlighting its importance for daily software development activities. The latest version brings notable improvements that tackle common development challenges, such as enhanced debugging workflows that are faster and more efficient. It also introduces robust, enterprise-level security controls that are designed to be unobtrusive, ensuring developers can maintain productivity without compromising on security. Additionally, seamless integration with AI tools is featured, facilitating modern development practices. Overall, Docker Desktop 4.50 is portrayed as a crucial tool for development teams aiming to build, secure, and deploy software effectively.
👉 [Read more](https://www.docker.com/blog/docker-desktop-4-50/)

## 🔹 Java - The Inside Java Newsletter: The Latest on JavaOne 2026
The Inside Java Newsletter for October 2025 is dedicated to the preparations for JavaOne 2026. It encourages readers to subscribe for updates and mentions that the event will take place in March 2026. Readers are invited to visit online resources like learn.java, dev.java, and inside.java for a variety of multimedia content designed for developers, learners, educators, and customers. The newsletter also provides options to view past issues, subscribe, and share the newsletter with friends.
👉 [Read more](https://inside.java/2025/11/12/inside-java-newsletter/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post introduces a new experimental garbage collector called Green Tea, which is included in Go version 1.25. This update aims to improve memory management and performance in Go applications. The Green Tea garbage collector is designed to be more efficient and reduce pause times during garbage collection, enhancing the overall user experience for developers using Go. The post likely provides details on how this new system works and its benefits compared to the previous garbage collection methods.
👉 [Read more](https://go.dev/blog/greenteagc)

