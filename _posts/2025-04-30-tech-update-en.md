# 🛠️ 2025-04-30 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Image Volumes graduate to beta!
The blog post discusses the promotion of the Image Volumes feature in Kubernetes from alpha to beta in version 1.33. Initially introduced in version 1.31, Image Volumes allow mounting of certain subdirectories of an image volume as read-only. The feature remains disabled by default due to limited support from container runtimes. CRI-O supports the feature since version 1.31 and will include beta support in v1.33. Containerd is also working on beta support. The major update for its beta release is the addition of `subPath` and `subPathExpr` mounts, which enable mounting specific subdirectories within a container volume. Additionally, three new kubelet metrics are introduced to monitor the use of image volumes. The post includes instructions for using subdirectories as `subPath` and encourages users to provide feedback through Slack or the SIG Node mailing list.
👉 [Read more](https://kubernetes.io/blog/2025/04/29/kubernetes-v1-33-image-volume-beta/)

## 🔹 Spring Boot - This Week in Spring - April 29th, 2025
The blog post, "This Week in Spring - April 29th, 2025," is a roundup of events and updates in the Spring ecosystem. The author, a Spring enthusiast, shares their upcoming schedule, which includes attending conferences such as Devoxx UK, CodeRemix Miami, and Spring IO in Barcelona. The post highlights numerous Spring releases, including Spring Boot 3.5.0-RC1, Spring gRPC 0.8.0, and various updates to Spring Modulith, Spring Vault, and Spring Authorization Server. The author also discusses a podcast episode with Simon Maple and shares several links to articles and videos that provide insights into Java and Spring technologies. Additionally, there is a focus on the importance of testing code and evaluating AI-generated code. The post ends with various recommended readings and videos related to Java and Spring.
👉 [Read more](https://spring.io/blog/2025/04/29/this-week-in-spring-april-29th-2025)

## 🔹 Docker - Docker Desktop 4.41: Docker Model Runner supports Windows, Compose, and Testcontainers integrations, Docker Desktop on the Microsoft Store
Docker Desktop 4.41 introduces significant enhancements aimed at improving the workflow for AI developers and teams handling large-scale environments. Key updates include the Docker Model Runner now supporting Windows, integration with Compose and Testcontainers, and the availability of Docker Desktop on the Microsoft Store. These updates are designed to enable faster building and smarter collaboration among development teams.
👉 [Read more](https://www.docker.com/blog/docker-desktop-4-41/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
The blog post titled "Finalizing the Java On-ramp - Inside Java Newscast #90" discusses upcoming changes in Java 25, highlighting a feature set called "Paving the On-ramp." This feature is expected to be finalized in the Java 25 release. Additionally, the post announces the launch of a new website, lear.java, aimed at individuals looking to learn Java or teach it. The newscast provides insights into these developments and their implications for the Java community.
👉 [Read more](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The tech blog post discusses improvements in benchmark looping introduced with Go 1.24, focusing on the new `testing.B.Loop` feature. This feature aims to provide more predictable and consistent benchmarking results by better managing how benchmarks are executed. It addresses issues related to variations in loop counts and execution times, enhancing the reliability of performance measurements in Go. The post highlights the benefits of these changes for developers seeking accurate and stable benchmarking outcomes.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be participating in KubeCon + CloudNativeCon EU 2025 in London from April 1 to April 4. The team will discuss the upcoming release of Helm 4 during talk sessions and at their booth in the Project Pavilion. Attendees are encouraged to engage with Helm maintainers and learn more about Helm-related activities scheduled throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

