# 🛠️ 2025-09-03 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Introducing CPU Manager Static Policy Option for Uncore Cache Alignment
The blog post discusses the introduction of a new CPU Manager Static Policy Option, "prefer-align-cpus-by-uncorecache," in Kubernetes v1.34, which has graduated to beta. This feature is designed to optimize performance for specific workloads on processors with a split uncore cache architecture by aligning CPUs to minimize cache latency and contention. It explains the concept of uncore cache, the benefits of cache-aware workload placement, and how this feature can improve throughput for certain applications, particularly in telco environments. The post also provides instructions on enabling this feature in Kubernetes and offers further reading resources for more detailed information. Additionally, it invites those interested to participate in the development and discussion of this feature through SIG Node meetings.
👉 [Read more](https://kubernetes.io/blog/2025/09/02/kubernetes-v1-34-prefer-align-by-uncore-cache-cpumanager-static-policy-optimization/)

## 🔹 Spring Boot - The Road to GA - Introduction
The blog post discusses the upcoming release of major versions for the Spring portfolio, including the fourth major generation for Spring Boot and the seventh for Spring Framework, set for November. The upgrades will maintain JDK 17 compatibility and include Jakarta EE 11 and other technologies like Kotlin 2 and Jackson 3. The blog series will introduce new capabilities weekly until the release, covering topics such as resilience features, API versioning, HTTP client enhancements, and more. The post encourages readers to check for updates and provide feedback on available milestones, acknowledging the community’s role in driving these developments.
👉 [Read more](https://spring.io/blog/2025/09/02/road_to_ga_introduction)

## 🔹 Docker - Broadcom’s New Bitnami Restrictions? Migrate Easily with Docker
The blog post discusses recent restrictions introduced by Broadcom on Bitnami, a platform known for simplifying the deployment of popular applications through prebuilt container images and Helm charts. Bitnami has been instrumental in aiding developers and operators within the open source and cloud-native community. The post highlights the impact these restrictions may have and suggests migrating to Docker as an alternative solution. Docker is presented as a way to easily transition from Bitnami, ensuring that teams can continue deploying applications like WordPress and PostgreSQL efficiently. The post emphasizes the importance of maintaining standardized installation and updates despite the changes.
👉 [Read more](https://www.docker.com/blog/broadcoms-new-bitnami-restrictions-migrate-easily-with-docker/)

## 🔹 Java - The Inside Java Newsletter: Java 25, AI World, JavaOne 2026!
The Inside Java Newsletter for August 2025 highlights the upcoming Java 25 release scheduled for September and the Java sessions at Oracle AI World in October. It also announces the JavaOne event set for March 2026. The newsletter covers updates from Java User Groups, community events, podcasts, and technical content from the Java Platform Group. Produced by the Java Developer Relations team, the newsletter encourages readers to explore multimedia content at learn.java, dev.java, and inside.java, and invites them to check the archives, subscribe, and share it with others.
👉 [Read more](https://inside.java/2025/09/02/inside-java-newsletter/)

## 🔹 Golang - Testing Time (and other asynchronicities)
The blog post titled "Testing Time (and other asynchronicities)" focuses on the challenges and methodologies involved in testing asynchronous code. It delves into the usage of the `testing/synctest` package, which is designed to facilitate the testing process for asynchronous operations. The content of the post is based on a talk presented at GopherCon Europe 2025, sharing insights and strategies for effectively handling asynchronous testing in Go programming. The post highlights key concepts and tools that can help developers ensure their asynchronous code is reliable and performs as expected.
👉 [Read more](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The Helm team is attending KubeCon + CloudNativeCon EU '25 in London from April 1-4. They are preparing for the release of Helm 4 later this year. Attendees can engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion for more information about Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

