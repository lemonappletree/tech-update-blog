# 🛠️ 2025-11-30 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
Kubernetes v1.35의 출시를 앞두고, 이 블로그 글은 v1.35 버전에서 예정된 주요 변경 사항들을 설명합니다. cgroup v1 지원이 제거될 예정이며, ipvs 모드가 kube-proxy에서 더 이상 지원되지 않습니다. 또한, containerd v1.y 지원도 중단될 예정이므로 최신 버전으로 업그레이드해야 합니다. 이외에도 노드 선언 기능, Pod 리소스의 직접 업데이트, Pod 인증서, taint의 숫자 값 지원, 사용자 네임스페이스, OCI 이미지를 볼륨으로 마운트하는 기능 등이 향상됩니다. v1.35 버전은 2025년 12월 17일에 출시될 예정이며, Kubernetes 커뮤니티의 의견과 참여를 환영합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - Towards Spring Tools 5 - Stereotypes and a new Structural View
이 기술 블로그 글은 Spring 프로젝트에서 개발자들이 사용하는 고수준 개념과 추상화를 다루고 있으며, Spring Tools가 이러한 개념을 중심으로 소스 코드를 분석하여 개발 환경에서 빠른 탐색과 개요 제공을 어떻게 돕는지를 설명합니다. 새로운 주요 릴리스에서는 jMolecules 2.0의 스테레오타입 개념을 통합하여 프로젝트를 논리적 구조 뷰로 시각화하는 기능을 도입했습니다. 이 뷰는 파일과 폴더 대신 스테레오타입으로 그룹화된 프로젝트 요소들을 보여주며, 사용자 정의 스테레오타입을 정의할 수 있는 유연성을 제공합니다. 또한, Spring Modulith를 사용하는 프로젝트의 경우 모듈 구조도 함께 고려됩니다. 마지막으로, Spring Tools 5의 최신 릴리스 후보에 대한 정보와 향후 AI 코딩 어시스턴트 통합에 대한 예고가 포함되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/28/towards-spring-tools-5-part2)

## 🔹 Docker - You Want Microservices, But Do You Really Need Them?
이 블로그 글은 마이크로서비스를 포기하고 모놀리식 아키텍처로 전환하여 비용을 90% 절감한 아마존의 사례를 다룹니다. 2023년 5월, 아마존은 Prime Video 서비스에 대해 이 전환을 결정했으며, 이는 마이크로서비스 인프라를 판매하여 매년 수십억 달러를 벌어들이는 AWS가 때때로 모놀리식 아키텍처가 더 나을 수 있음을 인정한 것입니다.
👉 [자세히 보기](https://www.docker.com/blog/do-you-really-need-microservices/)

## 🔹 Java - Garbage Collection in Java: Choosing the Correct Collector
이 블로그 글은 Java의 가비지 컬렉션(GC)에 대해 설명하며, 적절한 컬렉터를 선택하는 방법을 다룹니다. 가비지 컬렉션은 자동 메모리 관리의 한 형태로, 개발자가 저수준 메모리 관리 문제보다는 애플리케이션 로직에 집중할 수 있게 해주는 Java 플랫폼의 핵심 기능입니다. Java 플랫폼은 다양한 가비지 컬렉션 알고리즘을 구현하여 모든 종류의 작업 부하를 처리할 수 있도록 합니다. 기본 컬렉터인 G1은 종종 좋은 선택이지만, 사용 사례에 따라 다른 GC가 더 나은 성능을 제공할 수 있습니다. 이 글에서는 가비지 컬렉션의 기본 개념, 여러 컬렉터가 존재하는 이유, G1과 ZGC의 주요 특징, 다양한 컬렉터와 JDK 릴리스 간의 성능 차이에 대해 탐구합니다.
👉 [자세히 보기](https://inside.java/2025/11/29/devoxxbelgium-choose-correct-gc/)

## 🔹 Golang - Go’s Sweet 16
제목: Go의 16번째 생일  
요약: Go 프로그래밍 언어의 16번째 생일을 축하합니다!  
링크: [Go 블로그](https://go.dev/blog/16years)

이 블로그 글은 Go 언어의 탄생 16주년을 기념하며, 그동안의 발전과 성과를 되돌아보는 내용입니다. Go 언어는 간결함과 효율성을 강조하며, 많은 개발자들에게 사랑받고 있는 언어로 성장해왔습니다. 16년 동안 Go 커뮤니티는 지속적으로 확장되고 있으며, 앞으로도 Go 언어의 발전이 기대됩니다.
👉 [자세히 보기](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
헬름 4 출시: 11월 12일 수요일, KubeCon + CloudNativeCon에서 헬름 4 발표 중 헬름 v4.0.0이 출시되었습니다. 이는 6년 만에 처음으로 나온 헬름의 새로운 주요 버전입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-4-released)

