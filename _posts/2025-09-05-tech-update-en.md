# 🛠️ 2025-09-05 Tech Update Summary

## 🔹 Kubernetes - PSI Metrics for Kubernetes Graduates to Beta
The blog post announces that Pressure Stall Information (PSI) Metrics have graduated to Beta as of Kubernetes v1.34. PSI is a Linux kernel feature that measures resource pressure, providing insights into resource bottlenecks affecting application performance. PSI metrics, available for CPU, memory, and I/O, are categorized into 'some' and 'full' pressure, indicating different levels of resource contention. Kubernetes now allows the collection and exposition of these metrics through the Summary API and Prometheus, enabling detailed monitoring and alerting on resource pressure at various levels. The post provides steps to enable PSI metrics, such as ensuring nodes run on Linux kernel version 4.20 or later and enabling the KubeletPSI feature gate. It also highlights potential uses of PSI metrics, like identifying memory leaks, optimizing resource requests, and triggering autoscaling. The blog encourages users to try the feature and provide feedback as it moves towards a stable release.
👉 [Read more](https://kubernetes.io/blog/2025/09/04/kubernetes-v1-34-introducing-psi-metrics-beta/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Cloud guru Ryan Baxter
The blog post announces a podcast episode featuring Ryan Baxter, a notable contributor to Spring Cloud. The conversation with Ryan Baxter takes place live at the SpringOne 2025 event. The post is part of the "A Bootiful Podcast" series hosted for Spring fans.
👉 [Read more](https://spring.io/blog/2025/09/04/a-bootiful-podcast-ryan-baxter)

## 🔹 Docker - Hybrid AI Isn’t the Future — It’s Here (and It Runs in Docker)
The blog post discusses the concept of hybrid AI, which combines the benefits of running AI models in the cloud with those of using local models. Cloud-based AI models offer powerful capabilities, but they can lead to high and unpredictable costs. In contrast, local models ensure privacy and manageability of expenses, though they are typically smaller and less powerful. The use of Docker, a platform for developing, shipping, and running applications, is highlighted as a solution that enables the effective deployment and management of hybrid AI models. This approach allows organizations to balance the trade-offs between cost, performance, and data privacy.
👉 [Read more](https://www.docker.com/blog/hybrid-ai-and-how-it-runs-in-docker/)

## 🔹 Java - The Inside Java Newsletter: Java 25, AI World, JavaOne 2026!
The Inside Java Newsletter for August 2025 highlights the upcoming release of Java 25 in September, and discusses Java-focused sessions at the Oracle AI World event in October. It also announces the JavaOne event scheduled for March 2026. The newsletter consistently provides updates from Java User Groups, community events, podcasts, and technical content from the Java Platform Group developers. Produced by the Java Developer Relations team, the newsletter invites readers to explore various multimedia content available on learn.java, dev.java, and inside.java. Readers are encouraged to check out past newsletters, subscribe, and share with friends.
👉 [Read more](https://inside.java/2025/09/02/inside-java-newsletter/)

## 🔹 Golang - Testing Time (and other asynchronicities)
The blog post titled "Testing Time (and other asynchronicities)" delves into the challenges and methodologies of testing asynchronous code in programming. It highlights the intricacies involved in verifying the behavior and performance of code that does not execute in a linear fashion. The post also introduces and explores the `testing/synctest` package, which is designed to aid developers in testing asynchronous processes more effectively. The content is based on a talk presented at GopherCon Europe 2025, offering insights and practical solutions for developers dealing with asynchronous code in their projects.
👉 [Read more](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
The blog post announces that the Debian/Ubuntu Helm Apt repository is being relocated. Previously hosted at Balto, the repository will now be hosted at Buildkite. Users installing Helm with Apt should update their APT key and repository references according to the new installation instructions provided by Helm.
👉 [Read more](https://helm.sh/blog/debian-helm-repository-move/)

