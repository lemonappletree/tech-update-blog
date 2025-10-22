# 🛠️ 2025-10-22 Tech Update Summary

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
The blog post titled "7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)" shares insights and advice on avoiding common mistakes when working with Kubernetes. The author discusses seven pitfalls, including not setting resource requests and limits, underestimating liveness and readiness probes, relying solely on container logs, treating development and production environments the same, leaving outdated resources, diving too deep into networking too soon, and neglecting security and RBAC (Role-Based Access Control). For each pitfall, the author provides context, explains the potential consequences, and offers practical tips for avoidance based on personal experiences. The post emphasizes the importance of understanding Kubernetes' functionalities and applying best practices to prevent performance and security issues. The author encourages continued learning through official documentation and community engagement.
👉 [Read more](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Multi-Factor Authentication in Spring Security 7
The blog post discusses the integration of Multi-Factor Authentication (MFA) in Spring Security 7, a feature that has been anticipated since 2013. MFA enhances security by requiring multiple verification factors, which can include something the user knows (like a password), something they have (like a phone app), or something they are (like a fingerprint). The post explains how Spring Security 7 supports MFA, allowing for global or conditional requirements of multiple factors, time-based authentication, and user-based scenarios. It details how MFA is modeled using `GrantedAuthority` and describes enabling MFA globally with the `@EnableGlobalMultiFactorAuthentication` annotation. The post also covers customizing MFA rules using `AuthorizationManagerFactory` and implementing user-specific rules. Additionally, it provides guidance on how custom authentication providers can participate by issuing their own `FactorGrantedAuthority`. Finally, the blog suggests that MFA can help applications move towards passwordless authentication by using configurations like passkeys and biometric scans. For further exploration, the post recommends checking out sample code and documentation for more in-depth understanding.
👉 [Read more](https://spring.io/blog/2025/10/21/multi-factor-authentication-in-spring-security-7)

## 🔹 Docker - Introducing a Richer ”docker model run” Experience
The blog post announces a significant upgrade to the Docker Model Runner's interactive chat experience. This tool is used for running AI workloads locally, and the new enhancements aim to improve the command-line interface (CLI) experience for developers. By making the CLI more powerful and intuitive, the update seeks to transform potentially frustrating tasks into more enjoyable ones, enhancing productivity and user satisfaction.
👉 [Read more](https://www.docker.com/blog/docker-model-run-prompt/)

## 🔹 Java - Assembling Project Leyden #JVMLS
The blog post titled "Assembling Project Leyden #JVMLS" provides an update on Project Leyden's progress since John Rose's presentation two years ago at JVMLS. The project has made significant advancements, delivering Java Enhancement Proposals (JEPs) in JDK 24 and JDK 25. These JEPs are essential building blocks for developing new Ahead-Of-Time (AOT) compilation features. The post delves into the creation of the AOTCache, explaining the process and timing involved. It also outlines upcoming steps in the Leyden project, areas for future exploration, and some unexpected discoveries made by the team during development.
👉 [Read more](https://inside.java/2025/10/21/jvmls-assembling-project-leyden/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new diagnostic tool called "flight recorder" in Go version 1.25. This tool is designed to enhance the debugging and monitoring capabilities of Go applications by capturing detailed runtime information. The flight recorder helps developers identify and resolve issues more efficiently by providing insights into the application's behavior over time.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
The blog post celebrates the 10th anniversary of Helm, a tool that was created during a hackathon shortly after the release of Kubernetes 1.1.0. It highlights the initial commit made by Matt Butcher on October 19, 2015, marking the beginning of Helm's development. The first version of Helm, known as Helm Classic, can be found in its original Git repository. This was before Helm merged with Deployment Manager and became a part of the Kubernetes project. The post provides a link to the full story on Helm's official blog.
👉 [Read more](https://helm.sh/blog/helm-turns-ten/)

