# 🛠️ 2025-12-01 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
Kubernetes v1.35의 출시가 다가오면서 프로젝트는 지속적으로 발전하고 있습니다. 이번 릴리스에서는 cgroup v1 지원 제거, kube-proxy의 ipvs 모드 사용 중단, containerd v1.y 지원 종료 등이 예정되어 있습니다. 또한, 노드 선언 기능, Pod 자원 인플레이스 업데이트, Pod 인증서 기능, taint의 숫자 값 지원, 사용자 네임스페이스, OCI 이미지를 볼륨으로 마운트하는 지원 등 여러 개선 사항이 포함될 예정입니다. 이러한 변화들은 클러스터의 안정성과 성능을 향상시키고 Kubernetes의 현대적 기능을 지원하기 위한 것입니다. Kubernetes v1.35는 2025년 12월 17일에 출시될 예정입니다. 더 많은 정보는 Kubernetes 공식 블로그와 릴리스 노트를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - Towards Spring Tools 5 - Stereotypes and a new Structural View
이 기술 블로그 글은 Spring 프로젝트에서 개발자가 클래스와 인터페이스 같은 저수준 개념뿐만 아니라 서비스, 리포지토리, 구성 클래스, 엔티티 등과 같은 고수준 추상화 개념을 중심으로 작업할 때 도움이 되는 Spring Tools 5의 새로운 기능을 소개합니다. 기존에는 "Go To Symbol" 기능을 사용해 이러한 개념을 상징적으로 표현했지만, 이번 주요 업데이트에서는 jMolecules 2.0에서 소개된 '스테레오타입' 개념을 바탕으로 프로젝트의 논리적 구조를 시각화하는 기능을 도입했습니다. 이 논리적 구조 뷰는 파일과 폴더 대신 프로젝트의 요소를 스테레오타입별로 그룹화하여 보여주며, 사용자 정의 스테레오타입을 통해 구조 뷰를 맞춤화할 수 있습니다. 또한, Spring Modulith와 통합하여 모듈 구조도 반영합니다. Spring Tools 5의 최신 릴리스 후보는 도구 미리보기 페이지에서 확인할 수 있으며, AI 코딩 어시스턴트와의 새로운 통합도 곧 소개될 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/28/towards-spring-tools-5-part2)

## 🔹 Docker - You Want Microservices, But Do You Really Need Them?
이 기술 블로그 글은 마이크로서비스 대신 모놀리스를 선택했을 때 비용 절감의 사례를 소개합니다. 2023년 5월, 아마존은 프라임 비디오 서비스에서 마이크로서비스를 포기하고 모놀리스로 전환하여 비용을 90% 절감했습니다. 이는 마이크로서비스 인프라를 판매하여 막대한 수익을 올리는 AWS가 때때로 전통적인 모놀리스가 더 나은 선택이 될 수 있음을 인정한 사례입니다.
👉 [자세히 보기](https://www.docker.com/blog/do-you-really-need-microservices/)

## 🔹 Java - Garbage Collection in Java: Choosing the Correct Collector
Java의 가비지 컬렉션(GC)은 자동 메모리 관리의 한 형태로, Java 플랫폼의 핵심 기능입니다. 개발자는 메모리 관리의 세부 사항보다는 애플리케이션 로직에 집중할 수 있습니다. Java 플랫폼은 다양한 가비지 컬렉션 알고리즘을 구현하여 다양한 작업 부하를 처리할 수 있도록 해줍니다. 기본 컬렉터인 G1은 대체로 좋은 선택이지만, 사용 사례에 따라 다른 GC가 더 나은 성능을 제공할 수 있습니다. 이 글은 가비지 컬렉션의 기본 개념, 여러 컬렉터가 존재하는 이유, G1과 ZGC의 주요 특성, 컬렉터 및 JDK 버전에 따른 성능 차이를 탐구합니다.
👉 [자세히 보기](https://inside.java/2025/11/29/devoxxbelgium-choose-correct-gc/)

## 🔹 Golang - Go’s Sweet 16
블로그 글은 프로그래밍 언어 Go의 16번째 생일을 기념하는 내용입니다. Go 언어의 발전과 성과를 돌아보며, 커뮤니티의 기여와 앞으로의 비전에 대해 이야기합니다.
👉 [자세히 보기](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
제목: Helm 4 출시  
내용 요약: 11월 12일 수요일, KubeCon + CloudNativeCon 행사에서 Helm 4가 발표되며 Helm v4.0.0이 공식 출시되었습니다. 이는 6년 만에 처음으로 출시된 Helm의 주요 버전입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-4-released)

