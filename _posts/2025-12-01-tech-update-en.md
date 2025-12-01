# 🛠️ 2025-12-01 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
The blog post provides a preview of the upcoming Kubernetes v1.35 release, highlighting key changes and enhancements. The release will include significant deprecations and removals, such as the removal of cgroup v1 support, which will affect administrators using older Linux distributions, and the deprecation of ipvs mode in kube-proxy to streamline the codebase. Additionally, support for containerd v1.y will be deprecated, urging users to switch to version 2.0 or later.

The post also outlines several featured enhancements. The "node declared features" framework will allow nodes to report their supported features, improving scheduling accuracy and cluster stability. The in-place update of Pod resources will graduate to General Availability, allowing CPU and memory adjustments without restarting Pods. The post introduces pod certificates for native workload identity, numeric values for taints to enhance scheduling, user namespaces for improved security, and support for mounting OCI images as volumes to simplify data distribution.

Finally, the post invites readers to stay informed about the release, engage with the community through various channels, and explore the Kubernetes Special Interest Groups (SIGs) for further involvement. The Kubernetes v1.35 release is planned for December 17, 2025.
👉 [Read more](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - Towards Spring Tools 5 - Stereotypes and a new Structural View
The blog post discusses updates in Spring Tools 5, focusing on enhancing developers' experience by integrating higher-level Spring concepts like services and repositories into IDEs. Traditionally, Spring Tools used the "Go To Symbol" feature for navigation based on Spring-specific symbols. The new release, in collaboration with Spring Modulith and jMolecules, introduces a "logical structure view," which organizes project elements by stereotypes like controllers and repositories, rather than files and folders. This view allows customization of visible stereotypes, enhancing flexibility and control. The update also supports modular structures defined by Spring Modulith and introduces the ability to create custom stereotypes via the jMolecules framework. The blog promises future updates, including AI integration, in upcoming releases of Spring Tools 5.
👉 [Read more](https://spring.io/blog/2025/11/28/towards-spring-tools-5-part2)

## 🔹 Docker - You Want Microservices, But Do You Really Need Them?
The blog post discusses Amazon's decision to transition its Prime Video service from a microservices architecture to a monolithic one, resulting in a 90% cost reduction in May 2023. Despite being a major provider of microservices infrastructure through AWS, Amazon recognized that a monolithic approach could be more efficient in certain scenarios. This example highlights that while microservices offer various benefits, such as scalability and flexibility, they may not always be the most cost-effective or necessary solution for all applications. The post encourages tech leaders to carefully evaluate their needs before adopting microservices.
👉 [Read more](https://www.docker.com/blog/do-you-really-need-microservices/)

## 🔹 Java - Garbage Collection in Java: Choosing the Correct Collector
The blog post titled "Garbage Collection in Java: Choosing the Correct Collector" discusses the role of garbage collection (GC) as an important feature of the Java platform, which aids in automatic memory management. This feature allows developers to concentrate on application logic without worrying about memory management. Java offers various garbage collection algorithms to handle different workloads. While the default G1 collector is often a reliable choice, other collectors might offer better performance depending on specific use cases. The post includes a video that covers the fundamentals of garbage collection, the rationale behind having multiple collectors, the main features of G1 and ZGC, and the performance variations between different collectors and JDK versions.
👉 [Read more](https://inside.java/2025/11/29/devoxxbelgium-choose-correct-gc/)

## 🔹 Golang - Go’s Sweet 16
The blog post titled "Go’s Sweet 16" celebrates the 16th anniversary of the Go programming language. It highlights Go's journey since its inception, reflecting on the milestones achieved over the years. The post also discusses the growth of the Go community, the language's evolution, and its impact on software development. Additionally, it looks forward to Go's future, emphasizing continued innovation and community engagement.
👉 [Read more](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
The blog post announces the release of Helm v4.0.0, which occurred on Wednesday, November 12th, during a presentation at KubeCon + CloudNativeCon. This marks the first major update to Helm in six years.
👉 [Read more](https://helm.sh/blog/helm-4-released)

