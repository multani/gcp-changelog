# Service Extensions

## 2025-12-08

### Feature

You can use Service Extensions to implement [dynamic forwarding](https://docs.cloud.google.com/service-extensions/docs/lb-advanced-use-cases#dynamic-forwarding), which helps you map tenants to endpoints programmatically, without having to update your URL maps. This feature is in **Preview**.

---
## 2025-11-17

### Feature

For authorization extensions, in addition to the ext\_proc Envoy gRPC API, the
[ext\_authz gRPC API](https://docs.cloud.google.com/service-extensions/docs/callouts-overview##ext-authz) is also supported. This capability allows seamless integration with the broader authorization ecosystem. This feature is in **Preview**.

---
## 2025-11-13

### Feature

[Edge extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#edge-extensions) help you manipulate request headers early in the processing lifecycle of global external Application Load Balancers to influence caching and routing decisions. This feature is in **General Availability**.

### Feature

Regional external and internal Application Load Balancers support [route](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions#configure-route-plugins) and [traffic](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions#configure-traffic-plugins) extensions using plugins. This feature is in **Preview**.

---
## 2025-11-05

### Feature

[Cloud Load Balancing callouts](https://docs.cloud.google.com/service-extensions/docs/callouts-overview) have full duplex streaming support.

---
## 2025-10-28

### Feature

[Authorization extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions) help you configure Cloud Load Balancing authorization policies to use custom authorization engines. This feature is in **General Availability**.

---
## 2025-09-15

### Feature

To protect AI workloads, you can [configure traffic extensions to call the Model Armor service](https://cloud.google.com/service-extensions/docs/configure-extensions-to-google-services#configure-traffic-ma) on supported Application Load Balancers. This feature is in **General Availability**.

---
## 2025-07-24

### Feature

To [upload your Wasm plugin code](https://cloud.google.com/service-extensions/docs/prepare-plugin-code#generic-repository) to Artifact Registry, you can use generic format repositories, in addition to Docker repositories. This feature is in **Preview**.

---
## 2025-07-01

### Feature

[Plugins for Cloud Load Balancing](https://cloud.google.com/service-extensions/docs/overview#integration-lb-plugins) help you insert WebAssembly (Wasm) code in a fully managed serverless environment directly into the data path of most Cloud Load Balancing Application Load Balancers. This feature is in **General Availability**.

---
## 2025-06-23

### Feature

[Edge extensions](https://cloud.google.com/service-extensions/docs/lb-extensions-overview#edge-extensions) help you manipulate request headers early in the request processing lifecycle of global external Application Load Balancers to influence caching and routing decisions. This feature is in **Preview**.

Learn how to [configure an edge extension](https://cloud.google.com/service-extensions/docs/configure-edge-extensions).

---
