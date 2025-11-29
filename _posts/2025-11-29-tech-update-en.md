# 🛠️ 2025-11-29 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
The blog post provides a preview of the upcoming Kubernetes v1.35 release, highlighting key deprecations, removals, and enhancements. Significant changes include the removal of cgroup v1 support, deprecation of the ipvs mode in kube-proxy, and the final warning for containerd v1.x support, encouraging users to update to containerd 2.0 or later. The release also introduces several enhancements, such as node declared features for improved scheduling, in-place updates for Pod resources, and native support for Pod certificates to enhance workload security. Other features include numeric values for taints, user namespaces for improved security, and support for mounting OCI images as volumes. The release is scheduled for December 17, 2025, with further details to be announced in the official CHANGELOG. The post encourages community involvement through various channels and SIGs (Special Interest Groups).
👉 [Read more](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - Towards Spring Tools 5 - Stereotypes and a new Structural View
The tech blog post discusses enhancements in the upcoming release of Spring Tools 5, focusing on the integration of stereotypes and a new structural view for Spring projects. Traditionally, Spring Tools used a "Go To Symbol" feature to help developers navigate Spring concepts like services and repositories. The new release, in collaboration with Spring Modulith and jMolecules, elevates this by providing a logical structure view that visualizes projects based on stereotypes, grouping elements like web controllers and entities. This view offers customization options, allowing developers to select which stereotypes to display, and it accommodates custom stereotypes through jMolecules annotations or metadata files. Additionally, if a project uses Spring Modulith, the view will reflect its modular structure. The blog post also mentions upcoming features and invites developers to try the latest release candidates.
👉 [Read more](https://spring.io/blog/2025/11/28/towards-spring-tools-5-part2)

## 🔹 Docker - You Want Microservices, But Do You Really Need Them?
The blog post discusses the trend of adopting microservices architecture and questions whether it's always the best choice. It highlights a significant case: Amazon's decision to revert its Prime Video service from microservices back to a monolithic architecture, resulting in a 90% cost reduction in May 2023. Despite being a major provider of microservices infrastructure through AWS, Amazon acknowledged that a monolithic approach can sometimes be more efficient. The post suggests that while microservices offer advantages, it's crucial for organizations to evaluate their specific needs and consider whether a monolithic approach might be more beneficial.
👉 [Read more](https://www.docker.com/blog/do-you-really-need-microservices/)

## 🔹 Java - Help, My Java Object Vanished (and the GC is Not at Fault)
The blog post titled "Help, My Java Object Vanished (and the GC is Not at Fault)" explores the development of Project Valhalla and the intricacies of the HotSpot JVM. It explains how Java objects can seemingly disappear without the garbage collector being responsible. The article provides practical advice on using JVM flags to diagnose and resolve such issues. It also shares valuable lessons learned from debugging HotSpot, offering readers a deeper understanding of JVM internals and how to troubleshoot complex Java problems effectively.
👉 [Read more](https://inside.java/2025/11/28/markword/)

## 🔹 Golang - Go’s Sweet 16
The blog post celebrates the 16th anniversary of the Go programming language. It reflects on Go's journey since its inception, highlighting its growth and impact on the software development community. The post also discusses key milestones in Go's development, its adoption by developers worldwide, and the vibrant community that has contributed to its success. The blog expresses gratitude to the contributors and users who have supported Go over the years and looks forward to continued innovation and growth in the future.
👉 [Read more](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
The blog post announces the release of Helm v4.0.0, the first major update in six years, which was unveiled at KubeCon + CloudNativeCon on November 12th.
👉 [Read more](https://helm.sh/blog/helm-4-released)

